# Binary Search

**Topic:** Binary Search
- **LeetCode 連結:** [704. Binary Search](https://leetcode.com/problems/binary-search/)
- **難度:** Easy

## 題目描述

給定一個升序排列的整數陣列 `nums` 和一個目標值 `target`，在陣列中搜尋目標值並回傳其索引。若目標值不存在則回傳 -1。

## 解題思路

1. 設定搜尋範圍的左右邊界 `lo` 和 `hi`。
2. 計算中間位置 `mid`，比較 `nums[mid]` 與 `target`。
3. 若相等則回傳 `mid`；若 `nums[mid]` 較小則搜尋右半部；若較大則搜尋左半部。
4. 重複直到找到目標或搜尋範圍為空，回傳 -1。

## 程式碼

```python
# LeetCode 704. Binary Search
# Time: O(log n)  Space: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
```

## 複雜度分析

- **時間複雜度:** O(log n)
- **空間複雜度:** O(1)
