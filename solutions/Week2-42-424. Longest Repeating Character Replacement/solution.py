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
