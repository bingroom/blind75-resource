# 3Sum Closest

**Topic:** Array
- **LeetCode 連結:** [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
- **難度:** Medium

## 題目描述

給定一個整數陣列和目標值 target，找出陣列中三個數的和最接近 target 的值並回傳。

## 解題思路

1. 先將陣列排序。
2. 固定一個數，對剩餘部分使用雙指標搜尋。
3. 計算三數之和，若更接近目標值則更新答案。
4. 根據和與目標值的大小關係移動左或右指標。

## 程式碼

```python
# LeetCode 16. 3Sum Closest
# Time: O(n^2)  Space: O(1) (ignoring sort)

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Sort + two-pointer approach.
        Fix one element, then use two pointers on the remaining sorted
        subarray to find the pair that brings the total closest to target.
        """
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target  # exact match

        return closest
```

## 複雜度分析

- **時間複雜度:** O(n^2) -- sorting is O(n log n), then O(n) iterations each with an O(n) two-pointer scan.
- **空間複雜度:** O(1) -- ignoring the space used by sorting.
