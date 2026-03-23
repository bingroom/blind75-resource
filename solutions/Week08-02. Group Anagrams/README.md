# Group Anagrams

**Topic:** Hashing

- **LeetCode:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

 

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

	- There is no string in strs that can be rearranged to form `"bat"`.

	- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

	- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

 

**Constraints:**

	- `1 <= strs.length <= 10^4`

	- `0 <= strs[i].length <= 100`

	- `strs[i]` consists of lowercase English letters.

## Solution

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

## 思路

- **分組 key：** 將每個字串排序後當 key（或使用 tuple 字元計數），相同 key 的放同一組。用 defaultdict(list) 收集。

## 時間 / 空間複雜度

- **時間:** O(n · k log k)，n 為字串數，k 為最長字串長度（排序）。
- **空間:** O(n · k) 存輸出。

## 相關閱讀

- **資料結構:** Hash Table、defaultdict
- **演算法:** 排序當 key
