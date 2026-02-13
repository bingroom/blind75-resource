#!/usr/bin/env python3
LEETCODE_ACCOUNT = "bingroomkao@gmail.com"
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

LEETCODE_BASE = "https://leetcode.com"
GRAPHQL_URL = f"{LEETCODE_BASE}/graphql"

# GraphQL: 取得題目詳情（含 questionId，提交時必填）
PROBLEM_DETAIL_QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    titleSlug
    title
  }
}
"""


def get_credentials():
    session = os.environ.get("LEETCODE_SESSION")
    csrf = os.environ.get("LEETCODE_CSRF")
    
    # Use provided credentials if env vars are missing
    if not session:
        session = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjA5NTYyNzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhNTBhYTlmODI2YzEzZTQ1NTZjZGIzMjk5N2E4MDE1Yzc1NjQ2NGYzMTE0MjNlNzk3NjVlOWU1YmYxMmMxMTE0Iiwic2Vzc2lvbl91dWlkIjoiNGJiZWFkZWMiLCJpZCI6MjA5NTYyNzQsImVtYWlsIjoiYmluZ3Jvb21rYW9AZ21haWwuY29tIiwidXNlcm5hbWUiOiJuV1BNdE1VMEM4IiwidXNlcl9zbHVnIjoibldQTXRNVTBDOCIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9uV1BNdE1VMEM4L2F2YXRhcl8xNzcxMDAzMDg5LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc3MTAwNDk1OSwiaXAiOiIzNi4yMjkuMTYyLjg3IiwiaWRlbnRpdHkiOiJiNjA3MGY5N2RkOTlmZDFhMWY3MjkxNTZlZmQ2MWU4OSIsImRldmljZV93aXRoX2lwIjpbIjhhNjFhYzQ3NGE3YzkzMDQ3NmEzZjRhNmFjODNlMDQyIiwiMzYuMjI5LjE2Mi44NyJdfQ.xBDlpWlrUXndUK4hNbjLDq0SrTKOGTsHybyPIesP2dY"
    if not csrf:
        csrf = "Ko1kM9EfNLAmbZIEXGY2uxXMl2FlDNfZ"

    if not session or not csrf:
        print(
            "請設定環境變數 LEETCODE_SESSION 與 LEETCODE_CSRF（從瀏覽器 leetcode.com Cookie 取得）",
            file=sys.stderr,
        )
        sys.exit(1)
    return session, csrf


def get_headers(session: str, csrf: str):
    return {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Origin": LEETCODE_BASE,
        "Referer": f"{LEETCODE_BASE}/",
        "Cookie": f"LEETCODE_SESSION={session}; csrftoken={csrf}",
        "X-CSRFToken": csrf,
    }


def _request(url: str, method: str, headers: dict, data: dict = None) -> dict:
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(
        url,
        data=body,
        headers={**headers, "Accept": "application/json"},
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode() if e.fp else ""
        if e.code == 429:  # Too Many Requests：等待後重試一次
            time.sleep(15)
            req2 = urllib.request.Request(
                url,
                data=body,
                headers={**headers, "Accept": "application/json"},
                method=method,
            )
            with urllib.request.urlopen(req2, timeout=20) as resp2:
                return json.loads(resp2.read().decode())
        raise RuntimeError(f"HTTP {e.code}: {e.reason} | {err_body[:500]}") from e


def get_problem_detail(title_slug: str, session: str, csrf: str) -> dict:
    """取得題目詳情，包含 questionId（提交時必填）。"""
    data = _request(
        GRAPHQL_URL,
        "POST",
        get_headers(session, csrf),
        {"query": PROBLEM_DETAIL_QUERY, "variables": {"titleSlug": title_slug}},
    )
    if "errors" in data and data["errors"]:
        raise RuntimeError(f"GraphQL error: {data['errors']}")
    q = data.get("data", {}).get("question")
    if not q:
        raise RuntimeError(f"題目不存在: {title_slug}")
    return q


def submit_solution(
    title_slug: str, question_id: str, code: str, lang: str, session: str, csrf: str
) -> str:
    """提交程式碼，回傳 submission_id。"""
    url = f"{LEETCODE_BASE}/problems/{title_slug}/submit/"
    out = _request(
        url,
        "POST",
        get_headers(session, csrf),
        {"lang": lang, "typed_code": code, "question_id": question_id},
    )
    if "submission_id" not in out:
        raise RuntimeError(f"提交回應異常: {out}")
    return str(out["submission_id"])


def check_submission(submission_id: str, session: str, csrf: str) -> dict:
    """輪詢提交結果，直到 SUCCESS 或 FAILURE。"""
    url = f"{LEETCODE_BASE}/submissions/detail/{submission_id}/check/"
    for attempt in range(20):
        time.sleep(0.5 * (1.5 ** min(attempt, 4)))
        req = urllib.request.Request(
            url,
            headers=get_headers(session, csrf),
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        state = data.get("state")
        if state == "SUCCESS":
            return data
        if state == "FAILURE" or data.get("status_msg") == "Compile Error":
            return data
    raise TimeoutError("等待判題結果逾時")


def slug_from_solution_path(path: str) -> str:
    """從 solution 路徑推測題目 slug，例如 .../01-two-sum/solution.py -> two-sum。"""
    dirname = os.path.basename(os.path.dirname(path))
    m = re.match(r"^\d+-(.+)$", dirname)
    return m.group(1) if m else dirname


def main():
    parser = argparse.ArgumentParser(description="提交 LeetCode 程式碼並檢查 AC")
    parser.add_argument("solution_file", help="solution.py 路徑")
    parser.add_argument("--slug", help="題目 slug，例如 two-sum（若不提供則從路徑推測）")
    parser.add_argument("--lang", default="python3", help="語言 slug，預設 python3")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只列印會提交的資訊，不實際提交（仍需要 cookie 取得題目詳情）",
    )
    args = parser.parse_args()

    solution_path = args.solution_file
    if not os.path.isfile(solution_path):
        print(f"檔案不存在: {solution_path}", file=sys.stderr)
        sys.exit(1)

    slug = args.slug or slug_from_solution_path(solution_path)
    session, csrf = get_credentials()

    with open(solution_path, "r", encoding="utf-8") as f:
        code = f.read()

    print(f"題目 slug: {slug}")
    print("取得題目詳情...")
    problem = get_problem_detail(slug, session, csrf)
    question_id = problem["questionId"]
    title = problem.get("title", slug)
    print(f"題目: {title} (questionId={question_id})")

    if args.dry_run:
        print("--dry-run: 不提交")
        return

    print("提交中...")
    submission_id = submit_solution(slug, question_id, code, args.lang, session, csrf)
    print(f"submission_id: {submission_id}，等待判題...")
    result = check_submission(submission_id, session, csrf)

    status = result.get("status_msg", "Unknown")
    if status == "Accepted":
        print("結果: AC (Accepted)")
        # 紀錄 AC 的 time / space 排名到題目資料夾
        ac_record = {
            "status": "Accepted",
            "run_time": result.get("run_time"),
            "memory": result.get("memory"),
            "runtime_percentile": result.get("runtime_percentile"),
            "memory_percentile": result.get("memory_percentile"),
            "submission_id": submission_id,
            "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        out_dir = os.path.dirname(os.path.abspath(solution_path))
        rank_file = os.path.join(out_dir, "AC_result.json")
        with open(rank_file, "w", encoding="utf-8") as f:
            json.dump(ac_record, f, indent=2, ensure_ascii=False)
        print(f"已寫入: {rank_file}")
        if result.get("run_time"):
            print(f"  run_time: {result['run_time']}")
        if result.get("memory"):
            print(f"  memory: {result['memory']}")
        sys.exit(0)
    print(f"結果: {status}")
    if result.get("full_runtime_error"):
        print(result["full_runtime_error"])
    if result.get("full_compile_error"):
        print(result["full_compile_error"])
    if result.get("test_failed"):
        print("失敗測資:", result.get("input", ""))
    sys.exit(1)


if __name__ == "__main__":
    main()
