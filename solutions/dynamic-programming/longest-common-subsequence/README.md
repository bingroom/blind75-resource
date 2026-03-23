# Longest Common Subsequence

- **LeetCode:** [1250. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given two strings `text1` and `text2`, return *the length of their longest **common subsequence**. *If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

	- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

 

**Example 1:**

```

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

```

**Example 2:**

```

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

```

**Example 3:**

```

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

```

 

**Constraints:**

	- `1 <= text1.length, text2.length <= 1000`

	- `text1` and `text2` consist of only lowercase English characters.

## Solution

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

## 思路

- **二維 DP：** `dp[i][j]` = text1[:i] 與 text2[:j] 的 LCS。若 text1[i-1]==text2[j-1] 則 dp[i][j]=dp[i-1][j-1]+1，否則 dp[i][j]=max(dp[i-1][j], dp[i][j-1])。可壓成 O(n) 空間。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(min(m,n))。

## 相關閱讀

- **演算法:** Dynamic Programming、經典 LCS
