# LeetCode 42. Trapping Rain Water
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two-pointer approach.
        Water at any position = min(max_left, max_right) - height[i].
        Instead of precomputing both arrays, use two pointers converging
        inward. The smaller side determines the water level, because the
        taller side guarantees at least that much containment.
        """
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
