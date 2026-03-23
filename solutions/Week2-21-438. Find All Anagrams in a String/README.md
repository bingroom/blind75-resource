# Find All Anagrams in a String

**Topic:** String
- **LeetCode 連結:** [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- **難度:** Medium

## 題目描述

給定一個字串 s 和一個非空字串 p，找出 s 中所有是 p 的字母異位詞（anagram）的子字串，回傳這些子字串的起始索引。

## 解題思路

1. 統計字串 p 的字元頻率。
2. 在 s 上建立一個與 p 等長的滑動視窗，統計視窗內的字元頻率。
3. 每次滑動時，加入右側新字元、移除左側舊字元。
4. 若視窗內的頻率與 p 的頻率相同，將起始索引加入結果。

## 程式碼

```python
# LeetCode 438. Find All Anagrams in a String
# Time: O(n)  Space: O(1) — fixed 26-letter alphabet

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter(s[:len(p)])
        result = []

        if window == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            # Add new character entering the window
            window[s[i]] += 1
            # Remove character leaving the window
            old_char = s[i - len(p)]
            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]

            if window == p_count:
                result.append(i - len(p) + 1)

        return result
```

## 複雜度分析

- **時間複雜度:** O(n) where n = len(s)
- **空間複雜度:** O(1) -- at most 26 distinct characters in the counters
