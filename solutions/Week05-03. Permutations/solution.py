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
