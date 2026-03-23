# LeetCode 8. String to Integer (atoi)
# Time: O(n)  Space: O(1)


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
        i, n = 0, len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle optional sign
        sign = 1
        if i < n and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Read digits and convert
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result
