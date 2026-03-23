# LeetCode 16. 3Sum Closest
# Time: O(n^2)  Space: O(1) (ignoring sort)

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Sort + two-pointer approach.
        Fix one element, then use two pointers on the remaining sorted
        subarray to find the pair that brings the total closest to target.
        """
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target  # exact match

        return closest
