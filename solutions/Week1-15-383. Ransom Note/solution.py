# LeetCode 383. Ransom Note
# Time: O(m + n)  Space: O(1) — at most 26 lowercase letters

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Check if ransomNote can be constructed from magazine letters.
        Each letter in magazine can only be used once.
        """
        mag_count = Counter(magazine)
        for ch in ransomNote:
            if mag_count[ch] <= 0:
                return False
            mag_count[ch] -= 1
        return True
