# Longest Repeating Character Replacement

**Topic:** String
- **LeetCode 連結:** [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **難度:** Medium

## 題目描述

給定一個字串和一個整數 k，最多可以將字串中的 k 個字元替換為任意字母。求替換後能得到的最長連續相同字元子字串的長度。

## 解題思路

1. 使用滑動視窗，維護視窗內每個字元的出現次數和最大出現次數。
2. 擴展右邊界，將新字元加入計數並更新最大出現次數。
3. 若「視窗長度 - 最大出現次數 > k」，代表需替換的字元超過 k 個，收縮左邊界。
4. 持續更新最長視窗長度作為答案。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)（字母固定數量）。
