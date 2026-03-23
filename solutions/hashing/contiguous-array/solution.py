# LeetCode 525. Contiguous Array
# Time: O(n)  Space: O(n)


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        Find the maximum length subarray with equal number of 0s and 1s.
        Treat 0 as -1, then the problem becomes finding the longest subarray
        with sum == 0, which is solved by prefix-sum + hash map.
        """
        # Map from prefix_sum -> earliest index where that sum occurred
        prefix = {0: -1}
        max_len = 0
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1

            if running_sum in prefix:
                # Subarray from prefix[running_sum]+1 to i has sum 0
                max_len = max(max_len, i - prefix[running_sum])
            else:
                prefix[running_sum] = i

        return max_len
