# Ransom Note

**Topic:** Hash Table
- **LeetCode 連結:** [383. Ransom Note](https://leetcode.com/problems/ransom-note/)
- **難度:** Easy

## 題目描述

給定兩個字串 `ransomNote` 和 `magazine`，判斷是否能用 `magazine` 中的字母拼出 `ransomNote`。`magazine` 中每個字母只能使用一次。

## 解題思路

1. 使用雜湊表統計 `magazine` 中每個字母出現的次數。
2. 遍歷 `ransomNote` 的每個字母，檢查雜湊表中是否還有剩餘可用的該字母。
3. 若某字母的計數為 0 或不存在，回傳 `False`。
4. 否則將該字母的計數減 1，繼續遍歷。全部通過則回傳 `True`。

## 程式碼

```python
# LeetCode 383. Ransom Note
# Time: O(m + n)  Space: O(1) — at most 26 lowercase letters

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Check if ransomNote can be constructed from magazine letters.
        Each letter in magazine can only be used once.
        """
        mag_count = Counter(magazine)
        for ch in ransomNote:
            if mag_count[ch] <= 0:
                return False
            mag_count[ch] -= 1
        return True
```

## 複雜度分析

- **時間複雜度:** O(m + n) where m = len(ransomNote), n = len(magazine).
- **空間複雜度:** O(1) — the counter holds at most 26 lowercase English letters.
