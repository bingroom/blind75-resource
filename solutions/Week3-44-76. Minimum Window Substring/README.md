# Minimum Window Substring

**Topic:** String
- **LeetCode 連結:** [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- **難度:** Hard

## 題目描述

給定字串 s 和字串 t，找出 s 中包含 t 所有字元（含重複次數）的最短子字串。若不存在則回傳空字串。

## 解題思路

1. 使用 Counter 統計 t 中每個字元的需求次數。
2. 擴展右指標，遇到需要的字元時減少需求計數，當某字元需求降為 0 時滿足數加一。
3. 當所有字元需求皆滿足時，嘗試收縮左指標以找更短的子字串。
4. 收縮過程中若某字元需求回到正數，則滿足數減一，停止收縮。
5. 記錄過程中最短的合法子字串並回傳。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n + m)，n = len(s)，m = len(t)。
- **空間複雜度:** O(1)（字元集大小常數）。
