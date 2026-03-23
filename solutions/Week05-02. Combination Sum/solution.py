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
