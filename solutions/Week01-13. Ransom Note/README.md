# Ransom Note

**Topic:** Hashing

- **LeetCode:** [383. Ransom Note](https://leetcode.com/problems/ransom-note/)

## Problem Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise. Each letter in `magazine` can only be used once in `ransomNote`.


## Solution

```python
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
```

## Approach

1. Count the frequency of every character in `magazine` using a hash map.
2. Iterate through `ransomNote`. For each character, check if the count in the map is positive.
3. If a character is missing or exhausted, return `False`. Otherwise decrement the count and continue.
4. If we finish the loop, every character was available — return `True`.

## Complexity

- **Time:** O(m + n) where m = len(ransomNote), n = len(magazine).
- **Space:** O(1) — the counter holds at most 26 lowercase English letters.
