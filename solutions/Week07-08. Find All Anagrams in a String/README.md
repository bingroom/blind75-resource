# Find All Anagrams in a String

**Topic:** String

## Problem Description
Given two strings `s` and `p`, return a list of start indices of `p`'s anagrams in `s`. An anagram is a rearrangement of all characters.


## Solution

```python
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
```

## Approach
Sliding window of size `len(p)` over `s`. Maintain a frequency counter for the current window and compare it to the frequency counter of `p`. Slide the window by adding the new right character and removing the old left character.

## Complexity
- **Time:** O(n) where n = len(s)
- **Space:** O(1) -- at most 26 distinct characters in the counters
