# Combination Sum

**Topic:** Backtracking

- **LeetCode:** [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

## Problem Description

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. The same number may be chosen an unlimited number of times.


## Solution

```python
# LeetCode 39. Combination Sum
# Time: O(n^(target/min))  Space: O(target/min) recursion depth

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    continue
                path.append(c)
                # Pass i (not i+1) because we can reuse the same element
                backtrack(i, remaining - c, path)
                path.pop()

        backtrack(0, target, [])
        return result
```

## Approach

Use backtracking with a `start` index to avoid duplicate combinations.

1. At each step, iterate from `start` to end of candidates.
2. If the candidate does not exceed the remaining target, add it to the path and recurse with the same index (allowing reuse).
3. When remaining equals 0, add a copy of the path to the result.
4. Backtrack by removing the last element.

## Complexity

- **Time:** O(n^(target/min)) in the worst case, where min is the smallest candidate
- **Space:** O(target/min) for the recursion depth
