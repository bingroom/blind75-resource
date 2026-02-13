# LeetCode 70. Climbing Stairs
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        每次可爬 1 或 2 階，到第 n 階有幾種方法。dp[i] = dp[i-1] + dp[i-2]，可壓成兩變數。
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
