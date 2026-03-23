# LeetCode 50. Pow(x, n)
# Time: O(log n)  Space: O(1)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n & 1:  # n is odd
                result *= x
            x *= x
            n >>= 1

        return result
