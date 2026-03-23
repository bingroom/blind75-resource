# Longest Palindromic Substring

**Topic:** String
- **LeetCode 連結:** [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- **難度:** Medium

## 題目描述

給定一個字串 s，找出其中最長的迴文子字串。迴文是指正讀和反讀相同的字串。

## 解題思路

1. 以每個位置作為中心，向兩側擴展尋找迴文。
2. 分別處理奇數長度（單一中心）和偶數長度（相鄰兩字元為中心）的情況。
3. 擴展時，只要左右字元相同就繼續向外擴展。
4. 記錄過程中遇到的最長迴文子字串並回傳。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n²)。
- **空間複雜度:** O(1)。
