# Subsets

**Topic:** Backtracking

- **LeetCode:** [78. Subsets](https://leetcode.com/problems/subsets/)

## Problem Description

Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets.


## Solution

```python
# LeetCode 78. Subsets
# Time: O(n * 2^n)  Space: O(n) recursion depth

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path[:])  # Every path is a valid subset
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
```

## Approach

Backtracking where every node in the recursion tree is a valid subset.

1. At each recursive call, append the current path to the result (every prefix is a valid subset).
2. Iterate from `start` to the end of `nums` to pick the next element.
3. Add the element, recurse with `i + 1`, then backtrack.
4. Using `start` ensures each element is only considered once and avoids duplicates.

## Complexity

- **Time:** O(n * 2^n) -- 2^n subsets, each takes O(n) to copy
- **Space:** O(n) for the recursion depth
