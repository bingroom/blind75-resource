# LeetCode 283. Move Zeroes
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two-pointer approach. `write` marks the position where the next
        non-zero element should be placed. After one pass, all non-zero
        elements are at the front in original order; fill the rest with 0.
        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
