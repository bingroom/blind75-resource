# Find Minimum in Rotated Sorted Array

**Topic:** Binary Search
- **LeetCode 連結:** [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- **難度:** Medium

## 題目描述

給定一個已旋轉的升序無重複陣列，找出其中的最小值。要求時間複雜度為 O(log n)。

## 解題思路

1. 使用二分搜尋，比較中間元素與右端元素。
2. 若 nums[mid] > nums[right]，最小值在右半部分。
3. 否則最小值在左半部分（包含 mid）。
4. 收斂後回傳 nums[left]。

## 程式碼

```python
# LeetCode 153. Find Minimum in Rotated Sorted Array
# 時間複雜度: O(log n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        旋轉過的有序陣列（無重複），找最小值。用二分搜：比較 mid 與 right 決定往左或往右。
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # 若 nums[mid] > nums[hi]，最小值在右半 (mid+1 ~ hi)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                # 否則在左半或就是 mid（含 mid）
                hi = mid
        return nums[lo]
```

## 複雜度分析

- **時間複雜度:** O(log n)。
- **空間複雜度:** O(1)。
