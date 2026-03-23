# LeetCode 189. Rotate Array
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Three-reverse approach:
        To rotate right by k, reverse the whole array, then reverse
        the first k elements, then reverse the rest.
        Example: [1,2,3,4,5,6,7], k=3
          reverse all:   [7,6,5,4,3,2,1]
          reverse [0:3]: [5,6,7,4,3,2,1]
          reverse [3:]:  [5,6,7,1,2,3,4]
        """
        n = len(nums)
        k %= n  # handle k > n

        def reverse(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
