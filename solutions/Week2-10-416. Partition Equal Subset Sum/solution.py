# LeetCode 416. Partition Equal Subset Sum
# Time: O(n * target)  Space: O(target)

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        # dp[j] = True if we can form sum j using a subset of nums
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Traverse backwards to avoid using the same element twice (0/1 knapsack)
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
