# Longest Palindromic Substring

- **LeetCode:** [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

 

**Example 1:**

```

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

```

**Example 2:**

```

Input: s = "cbbd"
Output: "bb"

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consist of only digits and English letters.

## Solution

```python
# LeetCode 5. Longest Palindromic Substring
# 時間複雜度: O(n²)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        求最長迴文子字串。以每個位置（及相鄰兩位置）為中心向外擴展，取最長。
        """
        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        best = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1) if i + 1 < len(s) else ""
            longer = odd if len(odd) >= len(even) else even
            if len(longer) > len(best):
                best = longer
        return best

```

## 思路

- **中心擴展：** 以每個索引為「奇長迴文」中心、相鄰兩索引為「偶長迴文」中心，向外擴展直到不相等，記錄最長子字串。

## 時間 / 空間複雜度

- **時間:** O(n²)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Expand Around Center、Manacher（O(n) 進階）
