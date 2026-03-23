# LeetCode 322. Coin Change
# 時間複雜度: O(amount * len(coins))  空間複雜度: O(amount)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        用最少硬幣數湊出 amount，無法則 -1。dp[i] = 湊出 i 的最少硬幣數，枚舉最後一枚硬幣。
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
