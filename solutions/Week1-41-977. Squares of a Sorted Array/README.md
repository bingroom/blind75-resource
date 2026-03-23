# Squares of a Sorted Array

**Topic:** Array
- **LeetCode 連結:** [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
- **難度:** Easy

## 題目描述

給定一個按非遞減順序排列的整數陣列，回傳每個數字平方後的陣列，結果也需按非遞減排序。

## 解題思路

1. 使用雙指標分別指向陣列的頭和尾。
2. 比較兩端元素的絕對值，較大者的平方放入結果陣列的末端。
3. 對應指標向內移動，從後往前填充結果陣列。

## 程式碼

```python
# LeetCode 977. Squares of a Sorted Array
# Time: O(n)  Space: O(n)

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach filling result from the back.
        The largest square is always at one of the two ends of the
        sorted input (negative numbers square to large values).
        Compare absolute values of left and right, place the larger
        square at the current write position, and shrink inward.
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result
```

## 複雜度分析

- **時間複雜度:** O(n) -- single pass with two pointers.
- **空間複雜度:** O(n) -- for the output array.
