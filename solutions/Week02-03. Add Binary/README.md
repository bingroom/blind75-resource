# Add Binary

**Topic:** String

## Problem Description
Given two binary strings `a` and `b`, return their sum as a binary string.


## Solution

```python
# LeetCode 67. Add Binary
# Time: O(max(m, n))  Space: O(max(m, n))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))
```

## Approach
Simulate binary addition from right to left, tracking the carry. Process both strings simultaneously, appending each bit of the result. Reverse at the end.

## Complexity
- **Time:** O(max(m, n))
- **Space:** O(max(m, n)) for the result
