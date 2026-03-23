# LeetCode 377. Combination Sum IV (順序不同算不同)
# 時間複雜度: O(target * n)  空間複雜度: O(target)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        用 nums 中的數（可重複）湊出 target，順序不同算不同組合，求組合數。dp[i] = 湊出 i 的組合數。
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    dp[i] += dp[i - x]
        return dp[target]
