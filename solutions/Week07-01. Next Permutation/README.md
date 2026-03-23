# Next Permutation

**Topic:** Array

- **LeetCode:** [31. Next Permutation](https://leetcode.com/problems/next-permutation/)

## Problem Description

Given an array of integers `nums`, find the next lexicographically greater permutation of the numbers. If no such permutation exists (the array is sorted in descending order), rearrange it to the lowest possible order (ascending).

The replacement must be in-place and use only constant extra memory.


## Solution

```python
# LeetCode 31. Next Permutation
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        1. From the right, find the first index `i` where nums[i] < nums[i+1]
           (the "pivot"). Everything to the right of i is in descending order.
        2. Find the smallest element to the right of i that is larger than
           nums[i], swap them.
        3. Reverse the suffix after index i to get the smallest permutation
           of that suffix.
        If no pivot exists, the array is the last permutation -- reverse it
        to get the first.
        """
        n = len(nums)

        # Step 1: find the pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: find the successor to swap with
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## Approach

1. **Find the pivot:** Scan from right to left to find the first index `i` where `nums[i] < nums[i + 1]`. The suffix after `i` is non-increasing.
2. **Find the successor:** Scan from the right to find the smallest element larger than `nums[i]`, then swap them.
3. **Reverse the suffix:** Reverse the elements after index `i` to turn the descending suffix into ascending -- producing the smallest next permutation.

If no pivot is found, the entire array is descending, so reversing it gives the first permutation.

## Complexity

- **Time:** O(n) -- at most two linear scans plus one reverse.
- **Space:** O(1) -- all operations are in-place.
