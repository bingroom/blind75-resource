# LeetCode 41. First Missing Positive
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Index-marking (cyclic sort) approach.
        The answer must be in [1, n+1]. Place each value v in nums[v-1]
        by swapping. After placement, the first index i where
        nums[i] != i + 1 gives the answer.
        """
        n = len(nums)

        # Place each number at its "correct" index: value v -> index v-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] into its correct position
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        # The first position where nums[i] != i + 1 is the answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
