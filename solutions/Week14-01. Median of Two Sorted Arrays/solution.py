# LeetCode 4. Median of Two Sorted Arrays
# Time: O(log(min(m, n)))  Space: O(1)

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search on the shorter array to find the correct partition.
        We split both arrays so that the left half contains exactly
        (m + n + 1) // 2 elements. The partition is valid when
        max(left1, left2) <= min(right1, right2).
        """
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # partition index in nums1
            j = half - i              # partition index in nums2

            # Edge values: use -inf/+inf when a partition side is empty
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Valid partition found
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1  # move partition left in nums1
            else:
                left = i + 1   # move partition right in nums1

        return 0.0  # unreachable with valid input
