# Palindrome Number

**Topic:** Math
- **LeetCode 連結:** [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- **難度:** Easy

## 題目描述

給定一個整數，判斷它是否為迴文數。負數和以 0 結尾的非零數不是迴文。

## 解題思路

1. 排除負數和以 0 結尾的非零數。
2. 反轉數字的後半部分：每次取最後一位加到反轉數中，原數除以 10。
3. 當原數不大於反轉數時停止。
4. 比較原數與反轉數（偶數位）或反轉數除以 10（奇數位）。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(log n) -- we process half the digits
- **空間複雜度:** O(1)
