# LeetCode 62. Unique Paths
# 時間複雜度: O(m * n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        從左上到右下，只能向右或向下，求路徑數。dp[j] 可壓成一行，dp[j] += dp[j-1]。
        """
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]
