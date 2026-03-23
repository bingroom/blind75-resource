# Longest Palindrome

**Topic:** String
- **LeetCode 連結:** [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)
- **難度:** Easy

## 題目描述

給定一個由大小寫英文字母組成的字串 `s`，回傳用這些字母能組成的最長迴文的長度。字母區分大小寫。

## 解題思路

1. 統計每個字母出現的次數。
2. 迴文的兩側需要成對的字母，因此每個字母可貢獻 `count // 2 * 2` 個字元。
3. 若有任何字母出現奇數次，迴文的正中間可以再放一個字元，長度加 1。
4. 將所有配對數量加總（加上可能的中間字元）即為答案。

## 程式碼

```python
# LeetCode 409. Longest Palindrome
# Time: O(n)  Space: O(1) — at most 52 distinct characters

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        for count in counts.values():
            length += count // 2 * 2  # use pairs
            if count % 2 == 1:
                has_odd = True
        # One odd-count character can sit in the center
        if has_odd:
            length += 1
        return length
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(1) -- bounded by alphabet size
