# LeetCode 409. Longest Palindrome
# Time: O(n)  Space: O(1) — at most 52 distinct characters

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        for count in counts.values():
            length += count // 2 * 2  # use pairs
            if count % 2 == 1:
                has_odd = True
        # One odd-count character can sit in the center
        if has_odd:
            length += 1
        return length
