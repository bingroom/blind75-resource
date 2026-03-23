# Longest Common Subsequence

**Topic:** Unknown
- **LeetCode 連結:** [0. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- **難度:** Medium

## 題目描述

給定兩個字串，找出它們的最長公共子序列的長度。子序列不要求連續，但需保持相對順序。

## 解題思路

1. 使用動態規劃，dp[i][j] 表示 text1 前 i 個字元與 text2 前 j 個字元的 LCS 長度。
2. 若 text1[i-1] == text2[j-1]，則 dp[i][j] = dp[i-1][j-1] + 1。
3. 否則 dp[i][j] = max(dp[i-1][j], dp[i][j-1])。
4. 用一維陣列滾動優化空間複雜度。

## 程式碼

```python
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
```

## 複雜度分析

- **時間複雜度:** O(m×n)。
- **空間複雜度:** O(min(m,n))。
