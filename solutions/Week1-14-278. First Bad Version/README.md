# First Bad Version

**Topic:** Binary Search
- **LeetCode 連結:** [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
- **難度:** Easy

## 題目描述

你是產品經理，目前有 `n` 個版本 `[1, 2, ..., n]`。某個版本之後的所有版本都是壞的。給定一個 API `isBadVersion(version)` 可以判斷版本是否為壞版本，找出第一個壞版本，並盡量減少 API 呼叫次數。

## 解題思路

1. 使用二分搜尋，設定搜尋範圍 `lo = 1`、`hi = n`。
2. 計算中間版本 `mid`，呼叫 `isBadVersion(mid)` 檢查。
3. 若 `mid` 是壞版本，則第一個壞版本在 `[lo, mid]`，令 `hi = mid`。
4. 若 `mid` 不是壞版本，則第一個壞版本在 `[mid+1, hi]`，令 `lo = mid + 1`。
5. 當 `lo == hi` 時，即為第一個壞版本。

## 程式碼

```python
# LeetCode 278. First Bad Version
# Time: O(log n)  Space: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid          # mid might be the first bad version
            else:
                lo = mid + 1      # mid is good, search right half
        return lo
```

## 複雜度分析

- **時間複雜度:** O(log n)
- **空間複雜度:** O(1)
