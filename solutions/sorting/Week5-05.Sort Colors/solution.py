# LeetCode 75. Sort Colors
# Time: O(n)  Space: O(1)
# Dutch National Flag algorithm

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort in-place using three pointers."""
        lo, mid, hi = 0, 0, len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
                # Don't advance mid -- swapped element needs inspection
