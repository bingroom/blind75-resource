# Longest Common Prefix

**Topic:** String

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.


## Solution

```python
# LeetCode 14. Longest Common Prefix
# Time: O(S) where S = sum of all characters  Space: O(1)

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Compare characters column by column
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return strs[0][:i]
        return strs[0]
```

## Approach
Vertical scanning: compare characters at the same position across all strings. Stop when a mismatch is found or any string is exhausted.

## Complexity
- **Time:** O(S) where S is the sum of all characters in all strings
- **Space:** O(1)
