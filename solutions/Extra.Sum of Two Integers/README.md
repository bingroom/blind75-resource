# Sum of Two Integers

**Topic:** Unknown
- **LeetCode 連結:** [0. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- **難度:** Medium

## 題目描述

不使用加減運算子，計算兩個整數的和。

## 解題思路

1. 使用 XOR 計算「無進位和」。
2. 使用 AND 再左移一位計算「進位」。
3. 重複以上步驟直到進位為 0。
4. Python 需用 32 位遮罩處理無限位元的問題。

## 程式碼

```python
# LeetCode 371. Sum of Two Integers (不用 + - 做加法)
# 時間複雜度: O(1) 位元數常數  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        不用 + - 運算符實現兩整數之和。用 XOR 得「無進位和」，AND 左移 1 得進位，重複直到無進位。
        Python 需處理無限位元：用 32 位遮罩限制在 32 位整數內。
        """
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        a, b = a & MASK, b & MASK
        while b:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        return a if a <= MAX else ~(a ^ MASK)
```

## 複雜度分析

- **時間複雜度:** O(1)（位元數固定）。
- **空間複雜度:** O(1)。
