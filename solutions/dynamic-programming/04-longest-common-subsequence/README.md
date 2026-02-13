# Longest Common Subsequence

- **LeetCode:** [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求兩字串的**最長公共子序列**長度（子序列不必連續、順序需一致）。

## 思路

- **二維 DP：** `dp[i][j]` = text1[:i] 與 text2[:j] 的 LCS。若 text1[i-1]==text2[j-1] 則 dp[i][j]=dp[i-1][j-1]+1，否則 dp[i][j]=max(dp[i-1][j], dp[i][j-1])。可壓成 O(n) 空間。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(min(m,n))。

## 相關閱讀

- **演算法:** Dynamic Programming、經典 LCS
