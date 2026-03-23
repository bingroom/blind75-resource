# LeetCode 560. Subarray Sum Equals K
# Time: O(n)  Space: O(n)

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Count subarrays whose elements sum to k using prefix-sum + hash map.
        If prefix[i] - prefix[j] == k, then subarray (j, i] sums to k.
        """
        count = 0
        running_sum = 0
        # Map from prefix_sum -> number of times it has occurred
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # empty prefix

        for num in nums:
            running_sum += num
            # How many earlier prefixes equal running_sum - k?
            count += prefix_counts[running_sum - k]
            prefix_counts[running_sum] += 1

        return count
