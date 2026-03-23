# LeetCode 1143. Longest Common Subsequence
# 時間複雜度: O(m * n)  空間複雜度: O(min(m,n)) 可壓成一維
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        兩字串的最長公共子序列長度（不必連續）。dp[i][j] = text1[:i] 與 text2[:j] 的 LCS 長度。
        """
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                tmp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = tmp
        return dp[n]
