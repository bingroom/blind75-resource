# LeetCode 139. Word Break
# 時間複雜度: O(n² * m)  n=len(s), m=平均單詞長  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        判斷 s 是否可由 wordDict 中的單詞（可重複使用）拼接而成。dp[i] = s[:i] 可否被拆分。
        """
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]
