# LeetCode 125. Valid Palindrome
# NeetCode: https://neetcode.io/problems/is-palindrome?list=blind75
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        判斷是否為迴文（只考慮英數字、忽略大小寫與其他字元）。
        雙指針：左右往內，跳過非英數字，比較轉小寫後是否相同。
        """
        left, right = 0, len(s) - 1
        while left < right:
            # 跳過非英數字
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
