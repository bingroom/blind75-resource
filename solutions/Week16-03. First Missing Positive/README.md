# First Missing Positive

**Topic:** Array

- **LeetCode:** [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

## Problem Description

Given an unsorted integer array `nums`, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


## Solution

```python
# LeetCode 41. First Missing Positive
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Index-marking (cyclic sort) approach.
        The answer must be in [1, n+1]. Place each value v in nums[v-1]
        by swapping. After placement, the first index i where
        nums[i] != i + 1 gives the answer.
        """
        n = len(nums)

        # Place each number at its "correct" index: value v -> index v-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] into its correct position
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        # The first position where nums[i] != i + 1 is the answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
```

## Approach

**Index marking (cyclic sort):**

1. The answer is always in the range `[1, n + 1]` where `n` is the array length (by pigeonhole).
2. For each element, if its value `v` is in `[1, n]`, swap it to index `v - 1` (its "home" position). Repeat the swap at the current index until the current value is out of range or already in its correct spot.
3. After the placement pass, scan left to right. The first index `i` where `nums[i] != i + 1` means `i + 1` is missing.
4. If all positions are correct, return `n + 1`.

Each element is swapped at most once into its correct position, so the inner while loop runs O(n) total across all iterations.

## Complexity

- **Time:** O(n) -- each element moves to its final position at most once.
- **Space:** O(1) -- rearrangement is done in-place.
