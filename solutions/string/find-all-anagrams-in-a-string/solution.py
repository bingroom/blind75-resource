# LeetCode 438. Find All Anagrams in a String
# Time: O(n)  Space: O(1) — fixed 26-letter alphabet

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter(s[:len(p)])
        result = []

        if window == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            # Add new character entering the window
            window[s[i]] += 1
            # Remove character leaving the window
            old_char = s[i - len(p)]
            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]

            if window == p_count:
                result.append(i - len(p) + 1)

        return result
