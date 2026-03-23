# Permutations

- **LeetCode:** [46. Permutations](https://leetcode.com/problems/permutations/)

## Problem Description

Given an array `nums` of distinct integers, return all possible permutations in any order.


## Solution

```python
# LeetCode 46. Permutations
# Time: O(n * n!)  Space: O(n)

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path: List[int], used: set):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num in used:
                    continue
                used.add(num)
                path.append(num)
                backtrack(path, used)
                path.pop()
                used.remove(num)

        backtrack([], set())
        return result
```

## Approach

Classic backtracking with a used set to track which elements are already in the current permutation.

1. Maintain a `path` list and a `used` set.
2. At each level, iterate over all nums. Skip any already in `used`.
3. Add the number to `path` and `used`, recurse, then remove (backtrack).
4. When `path` reaches the length of `nums`, record a copy.

## Complexity

- **Time:** O(n * n!) -- n! permutations, each takes O(n) to copy
- **Space:** O(n) for the recursion stack and used set
