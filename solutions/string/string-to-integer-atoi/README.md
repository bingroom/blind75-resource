# String to Integer (atoi)

## Problem Description
Implement the `myAtoi` function which converts a string to a 32-bit signed integer. Handle leading whitespace, optional sign, digit conversion, and clamp to the 32-bit signed integer range.

## Approach
Process the string in three stages: (1) skip leading whitespace, (2) detect optional sign, (3) read consecutive digits while checking for overflow before each multiplication. Clamp to `[-2^31, 2^31 - 1]` on overflow.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
