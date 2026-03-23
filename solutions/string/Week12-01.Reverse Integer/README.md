# Reverse Integer

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing causes overflow outside the 32-bit signed integer range `[-2^31, 2^31 - 1]`, return 0.


## Solution

```python
# LeetCode 7. Reverse Integer
# Time: O(log x)  Space: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0
        while x:
            digit = x % 10
            x //= 10
            result = result * 10 + digit

        result *= sign
        # Return 0 if overflow
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
```

## Approach
Extract digits from the end using modulo, build the reversed number by multiplying by 10 and adding each digit. Handle the sign separately and check for 32-bit overflow at the end.

## Complexity
- **Time:** O(log x) -- number of digits
- **Space:** O(1)
