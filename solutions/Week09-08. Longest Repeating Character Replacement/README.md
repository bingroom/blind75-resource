# Longest Repeating Character Replacement

**Topic:** String

- **LeetCode:** [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

 

**Example 1:**

```

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

```

**Example 2:**

```

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of only uppercase English letters.

	- `0 <= k <= s.length`

## Solution

```python
# LeetCode 424. Longest Repeating Character Replacement
# 時間複雜度: O(n)  空間複雜度: O(1) 最多 26 個字元
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        可將最多 k 個字元替換成任意字元，求最長「同一字元」連續子字串長度。
        滑窗：窗內「長度 - 最多出現次數」≤ k 時可擴右，否則縮左。
        """
        count = Counter()
        left = 0
        max_freq = 0
        best = 0
        for right, c in enumerate(s):
            count[c] += 1
            max_freq = max(max_freq, count[c])
            # 若替換數 (窗長 - max_freq) > k，縮左
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best

```

## 思路

- **滑動視窗：** 窗內「長度 − 出現次數最多的字元數」= 需替換數。若 ≤ k 可擴右；否則縮左。用 Counter 維護頻率，並維護「窗內最大頻率」以判斷是否合法。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)（字母固定數量）。

## 相關閱讀

- **演算法:** Sliding Window、Counter
