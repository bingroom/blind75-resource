# Palindrome Number

**Topic:** String

## Problem Description
Given an integer `x`, return true if `x` is a palindrome. Solve it without converting the integer to a string.


## Solution

```python
# LeetCode 9. Palindrome Number
# Time: O(log n)  Space: O(1)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even-length: x == reversed_half
        # For odd-length: x == reversed_half // 10 (drop the middle digit)
        return x == reversed_half or x == reversed_half // 10
```

## Approach
Reverse only the second half of the number. Compare the first half with the reversed second half. For odd-length numbers, discard the middle digit from the reversed half by dividing by 10.

## Complexity
- **Time:** O(log n) -- we process half the digits
- **Space:** O(1)
