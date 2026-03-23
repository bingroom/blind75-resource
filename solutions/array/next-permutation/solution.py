# LeetCode 31. Next Permutation
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        1. From the right, find the first index `i` where nums[i] < nums[i+1]
           (the "pivot"). Everything to the right of i is in descending order.
        2. Find the smallest element to the right of i that is larger than
           nums[i], swap them.
        3. Reverse the suffix after index i to get the smallest permutation
           of that suffix.
        If no pivot exists, the array is the last permutation -- reverse it
        to get the first.
        """
        n = len(nums)

        # Step 1: find the pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: find the successor to swap with
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
