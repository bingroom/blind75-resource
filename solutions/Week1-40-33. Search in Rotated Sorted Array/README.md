# Search in Rotated Sorted Array

**Topic:** Binary Search
- **LeetCode 連結:** [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- **難度:** Medium

## 題目描述

給定一個經過旋轉的升序排列整數陣列（無重複元素）和一個目標值，回傳目標值的索引。若不存在則回傳 -1，要求時間複雜度為 O(log n)。

## 解題思路

1. 使用二分搜尋，設定 lo 和 hi 指標。
2. 計算 mid，若 nums[mid] 等於 target 則直接回傳。
3. 判斷左半段 [lo..mid] 是否有序：若有序且 target 在此範圍內，縮小右邊界；否則搜尋右半段。
4. 若右半段有序且 target 在此範圍內，縮小左邊界；否則搜尋左半段。
5. 迴圈結束仍未找到則回傳 -1。

## 程式碼

```python
# LeetCode 33. Search in Rotated Sorted Array
# 時間複雜度: O(log n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        在旋轉過的有序陣列（無重複）中找 target 的索引，沒有則回傳 -1。
        二分：先判斷左半或右半哪一段是有序的，再判斷 target 是否落在該段內。
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            # 左半 [lo..mid] 為有序
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # 右半 [mid..hi] 為有序
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
```

## 複雜度分析

- **時間複雜度:** O(log n)。
- **空間複雜度:** O(1)。
