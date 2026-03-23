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
