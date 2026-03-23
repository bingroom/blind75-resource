# Valid Anagram

**Topic:** String
- **LeetCode 連結:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- **難度:** Easy

## 題目描述

給定兩個字串 `s` 和 `t`，判斷 `t` 是否為 `s` 的字母異位詞（anagram）。字母異位詞是指由相同字母重新排列而成的字串。

## 解題思路

1. 分別統計兩個字串中每個字元出現的次數。
2. 比較兩個計數結果是否完全相同。
3. 若相同則為字母異位詞，回傳 `True`；否則回傳 `False`。

## 程式碼

```python
# LeetCode 242. Valid Anagram
# 時間複雜度: O(n)  空間複雜度: O(1) 字元集常數
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        判斷 t 是否為 s 的 anagram（同字母異序）。兩邊字元計數相同即可。
        """
        return Counter(s) == Counter(t)
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)（字母表固定）。
