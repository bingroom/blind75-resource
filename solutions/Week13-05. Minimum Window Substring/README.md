# Minimum Window Substring

**Topic:** String

- **LeetCode:** [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring**** of *`s`* such that every character in *`t`* (**including duplicates**) is included in the window*. If there is no such substring, return *the empty string *`""`.

The testcases will be generated such that the answer is **unique**.

 

**Example 1:**

```

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

```

**Example 2:**

```

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

```

**Example 3:**

```

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

```

 

**Constraints:**

	- `m == s.length`

	- `n == t.length`

	- `1 <= m, n <= 10^5`

	- `s` and `t` consist of uppercase and lowercase English letters.

 

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

## Solution

```python
# LeetCode 76. Minimum Window Substring
# 時間複雜度: O(n + m)  空間複雜度: O(1) 字元集常數
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        求 s 中最短子字串，使得包含 t 中所有字元（含次數）。滑窗 + 計數滿足條件時縮左。
        """
        need = Counter(t)
        have = 0
        required = len(need)
        left = 0
        start, length = 0, float("inf")
        for right, c in enumerate(s):
            if c in need:
                need[c] -= 1
                if need[c] == 0:
                    have += 1
            while have == required:
                if right - left + 1 < length:
                    start, length = left, right - left + 1
                if s[left] in need:
                    if need[s[left]] == 0:
                        have -= 1
                    need[s[left]] += 1
                left += 1
        return s[start : start + length] if length != float("inf") else ""

```

## 思路

- **滑動視窗：** 用 need = Counter(t) 表示還缺多少；右擴時減少 need，當「滿足條件的字元種類數」= len(need) 時嘗試縮左以得到最小窗，並更新起點與長度。

## 時間 / 空間複雜度

- **時間:** O(n + m)，n = len(s)，m = len(t)。
- **空間:** O(1)（字元集大小常數）。

## 相關閱讀

- **演算法:** Sliding Window、Hash Table、Counter
