# Valid Anagram

- **LeetCode:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

**Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

 

**Constraints:**

	- `1 <= s.length, t.length <= 5 * 10^4`

	- `s` and `t` consist of lowercase English letters.

 

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

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

## 思路

- **計數：** 比較兩字串的字元頻率是否相同，例如 `Counter(s) == Counter(t)`。長度不同可先直接回傳 False。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)（字母表固定）。

## 相關閱讀

- **資料結構:** Hash Table、Counter
