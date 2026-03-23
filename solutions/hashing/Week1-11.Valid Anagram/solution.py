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
