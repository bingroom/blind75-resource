# Backspace String Compare

## Problem Description
Given two strings `s` and `t`, return true if they are equal when both are typed into empty text editors. `#` means a backspace character.


## Solution

```python
# LeetCode 844. Backspace String Compare
# Time: O(m + n)  Space: O(1)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Two-pointer approach from the end to achieve O(1) space
        i, j = len(s) - 1, len(t) - 1
        skip_s = skip_t = 0

        while i >= 0 or j >= 0:
            # Find next valid char in s
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            # Find next valid char in t
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # Compare characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False  # one string is exhausted but the other isn't

            i -= 1
            j -= 1

        return True
```

## Approach
Use two pointers starting from the end of each string. Track how many backspaces to apply (`skip` counter). When encountering `#`, increment skip; when skip > 0 on a regular character, decrement skip and move on. Compare the next valid characters from both strings.

## Complexity
- **Time:** O(m + n)
- **Space:** O(1)
