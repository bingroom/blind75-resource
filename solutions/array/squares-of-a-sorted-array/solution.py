# LeetCode 977. Squares of a Sorted Array
# Time: O(n)  Space: O(n)

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach filling result from the back.
        The largest square is always at one of the two ends of the
        sorted input (negative numbers square to large values).
        Compare absolute values of left and right, place the larger
        square at the current write position, and shrink inward.
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result
