# Squares of a Sorted Array

**Topic:** Array

- **LeetCode:** [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


## Solution

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

## Approach

Use a **two-pointer** technique:

1. Place pointers at the leftmost and rightmost elements.
2. The largest squared value must come from one of these two ends (large negatives or large positives).
3. Compare `abs(nums[left])` and `abs(nums[right])`. Place the larger square at the back of the result array.
4. Move the chosen pointer inward and repeat, filling the result from right to left.

## Complexity

- **Time:** O(n) -- single pass with two pointers.
- **Space:** O(n) -- for the output array.
