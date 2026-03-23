# Roman to Integer

## Problem Description
Given a roman numeral string, convert it to an integer. Roman numerals use subtractive notation for cases like IV (4) and IX (9).


## Solution

```python
# LeetCode 13. Roman to Integer
# Time: O(n)  Space: O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            # If current value < next value, subtract (e.g., IV = 4)
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]
        return result
```

## Approach
Iterate through the string. If the current symbol's value is less than the next symbol's value, subtract it (subtractive case); otherwise add it.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
