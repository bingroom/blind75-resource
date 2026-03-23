# Group Anagrams

**Topic:** String
- **LeetCode 連結:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- **難度:** Medium

## 題目描述

給定一組字串，將所有字母異位詞（anagram）分在同一組並回傳。字母異位詞是指由相同字母重新排列組成的字串。

## 解題思路

1. 建立一個雜湊表，key 為排序後的字串，value 為對應的原始字串列表。
2. 遍歷每個字串，將其排序後作為 key。
3. 將原始字串加入對應 key 的列表中。
4. 回傳雜湊表中所有的列表。

## 程式碼

```python
# LeetCode 49. Group Anagrams
# 時間複雜度: O(n * k log k)  k 為最長字串長  空間複雜度: O(n * k)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        將 anagram 分在同一組。用「排序後字串」或「tuple 計數」當 key 分組。
        """
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
```

## 複雜度分析

- **時間複雜度:** O(n · k log k)，n 為字串數，k 為最長字串長度（排序）。
- **空間複雜度:** O(n · k) 存輸出。
