# LeetCode 198. House Robber
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        相鄰不能同時偷，求最大金額。dp[i] = 考慮前 i 間的最大值，偷 i 則加 nums[i]+dp[i-2]，不偷則 dp[i-1]。
        """
        if not nums:
            return 0
        prev, cur = 0, nums[0]
        for i in range(1, len(nums)):
            prev, cur = cur, max(cur, prev + nums[i])
        return cur
