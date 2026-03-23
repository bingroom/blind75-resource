# Palindromic Substrings

**Topic:** Unknown
- **LeetCode 連結:** [0. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- **難度:** Medium

## 題目描述

給定一個字串，計算其中迴文子字串的總數。

## 解題思路

1. 以每個位置為中心，向兩側擴展尋找迴文。
2. 分別處理奇數長度（單字元中心）和偶數長度（雙字元中心）。
3. 每次成功擴展（兩端字元相同），計數加 1。

## 程式碼

```python
# LeetCode 647. Palindromic Substrings
# 時間複雜度: O(n²)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        計算迴文子字串的個數。以每個位置為中心向外擴展，每擴展成功一次就多一個迴文。
        """
        n = len(s)
        count = 0

        def expand(l: int, r: int) -> None:
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return count
```

## 複雜度分析

- **時間複雜度:** O(n²)。
- **空間複雜度:** O(1)。
