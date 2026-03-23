# LeetCode 136. Single Number
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR cancels out pairs, leaving the single number
        return result
