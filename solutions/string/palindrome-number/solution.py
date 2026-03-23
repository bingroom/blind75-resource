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
