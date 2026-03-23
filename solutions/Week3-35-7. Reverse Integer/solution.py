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
