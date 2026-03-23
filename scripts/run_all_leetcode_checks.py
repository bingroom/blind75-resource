#!/usr/bin/env python3
"""
批次對 blind75-resource 內所有 solution.py 執行 LeetCode 提交並檢查 AC。
會呼叫 leetcode_submit.py，AC 時會自動寫入該題目資料夾的 AC_result.json。
非 AC 的題目會列在報告中供修正。
"""

import json
import os
import re
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
SOLUTIONS_DIR = os.path.join(ROOT, "solutions")

# 路徑（相對於專案 ROOT）-> LeetCode 題目 slug 覆寫（若資料夾名與 LeetCode 不一致）
SLUG_OVERRIDES = {
    "solutions/tree/13-add-and-search-word-data-structure-design": "design-add-and-search-words-data-structure",
    "solutions/tree/design-add-and-search-words-data-structure": "design-add-and-search-words-data-structure",
    "solutions/graph/01-matrix": "01-matrix",
}


def slug_from_path(rel_path: str) -> str:
    """e.g. array/01-two-sum/solution.py -> two-sum"""
    parts = rel_path.replace("\\", "/").split("/")
    if len(parts) >= 2:
        dirname = parts[-2]
        m = re.match(r"^\d+-(.+)$", dirname)
        return m.group(1) if m else dirname
    return ""


def collect_solution_paths(skip_ac: bool = False):
    """skip_ac=True 時略過已有 AC_result.json 的題目（resume 用）。"""
    out = []
    for root, _dirs, files in os.walk(SOLUTIONS_DIR):
        if "solution.py" not in files:
            continue
        if skip_ac and "AC_result.json" in files:
            continue
        full = os.path.join(root, "solution.py")
        rel = os.path.relpath(full, ROOT)
        rel_dir = os.path.relpath(root, ROOT)
        slug = SLUG_OVERRIDES.get(rel_dir) or slug_from_path(rel)
        out.append((os.path.join(ROOT, rel), slug, rel))
    return sorted(out, key=lambda x: x[2])


def main():
    import argparse as ap
    p = ap.ArgumentParser()
    p.add_argument("--resume", action="store_true", help="只檢查尚未 AC 的題目（略過已有 AC_result.json 者）")
    args, _ = p.parse_known_args()
    paths = collect_solution_paths(skip_ac=args.resume)
    print(f"共 {len(paths)} 題待檢查" + (" (resume 模式)" if args.resume else "") + "\n")
    ac_list = []
    fail_list = []
    for i, (abspath, slug, rel) in enumerate(paths, 1):
        print(f"[{i}/{len(paths)}] {rel} (slug={slug})")
        cmd = [
            sys.executable,
            os.path.join(SCRIPT_DIR, "leetcode_submit.py"),
            abspath,
            "--slug",
            slug,
        ]
        try:
            result = subprocess.run(
                cmd,
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=90,
            )
            out = (result.stdout or "") + (result.stderr or "")
            if result.returncode == 0:
                ac_list.append((rel, slug))
                # 印出最後幾行即可
                for line in out.strip().split("\n")[-5:]:
                    print(f"  {line}")
            else:
                fail_list.append((rel, slug, out))
                print(f"  FAIL: {out[:500]}")
        except subprocess.TimeoutExpired:
            fail_list.append((rel, slug, "Timeout"))
            print("  FAIL: Timeout")
        except Exception as e:
            fail_list.append((rel, slug, str(e)))
            print(f"  FAIL: {e}")
        # 避免 LeetCode rate limit：每次提交間隔 5 秒
        if i < len(paths):
            time.sleep(5)
        print()
    # 報告
    report_path = os.path.join(ROOT, "scripts", "leetcode_batch_report.json")
    report = {
        "total": len(paths),
        "ac_count": len(ac_list),
        "ac": [{"rel": r, "slug": s} for r, s in ac_list],
        "fail_count": len(fail_list),
        "fail": [{"rel": r, "slug": s, "output": o[:2000]} for r, s, o in fail_list],
    }
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print("=" * 60)
    print(f"AC: {len(ac_list)} / {len(paths)}")
    print(f"失敗: {len(fail_list)}，詳見 {report_path}")
    if fail_list:
        for r, s, _ in fail_list:
            print(f"  - {r} ({s})")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
