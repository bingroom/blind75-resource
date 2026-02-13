# 自動提交 LeetCode 並檢查 AC

## 取得 Cookie（必填）

1. 在瀏覽器登入 [LeetCode](https://leetcode.com)。
2. 開啟開發者工具 (F12) → **Application** → **Cookies** → `https://leetcode.com`。
3. 複製以下兩個值：
   - **LEETCODE_SESSION**
   - **csrftoken**

## 設定環境變數並執行

```bash
cd /Users/bingroom/Documents/coding/blind75-resource
export LEETCODE_SESSION="你的 LEETCODE_SESSION 值"
export LEETCODE_CSRF="你的 csrftoken 值"
python scripts/leetcode_submit.py solutions/array/01-two-sum/solution.py
```

若題目 slug 無法從路徑推測，可手動指定：

```bash
python scripts/leetcode_submit.py solutions/array/01-two-sum/solution.py --slug two-sum
```

僅列印將提交的題目、不實際提交：

```bash
python scripts/leetcode_submit.py solutions/array/01-two-sum/solution.py --dry-run
```

僅使用 Python 3 標準庫，無需 `pip install`。

## 輸出

- **AC**：結果為 `Accepted`，腳本 exit 0，並在該題目資料夾寫入 **AC_result.json**（含 `run_time`、`memory`、`runtime_percentile`、`memory_percentile` 等，依 LeetCode 回傳為準）。
- **非 AC**：印出 `status_msg`、編譯/執行錯誤等，exit 1。

## 批次檢查全部題目

```bash
python3 scripts/run_all_leetcode_checks.py
```

- 每次提交間隔 5 秒以降低 429 機率；遇 429 會自動等待 15 秒重試一次。
- 報告寫入 `scripts/leetcode_batch_report.json`。

只檢查「尚未 AC」的題目（略過已有 `AC_result.json` 的資料夾）：

```bash
python3 scripts/run_all_leetcode_checks.py --resume
```

建議：若中途因 rate limit 失敗，可稍後再執行一次 `--resume` 補跑剩餘題目。

**若出現 HTTP 403 Forbidden**：多為 Cookie 過期或 LeetCode 阻擋。請重新登入 [leetcode.com](https://leetcode.com)，從開發者工具複製最新的 `LEETCODE_SESSION` 與 `csrftoken` 再執行。
