# Roman to Integer

## Problem Description
Given a roman numeral string, convert it to an integer. Roman numerals use subtractive notation for cases like IV (4) and IX (9).

## Approach
Iterate through the string. If the current symbol's value is less than the next symbol's value, subtract it (subtractive case); otherwise add it.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
