# Sum of Two Integers

**Topic:** Bit Manipulation

- **LeetCode:** [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given two integers `a` and `b`, return *the sum of the two integers without using the operators* `+` *and* `-`.

 

**Example 1:**

```
Input: a = 1, b = 2
Output: 3

```

**Example 2:**

```
Input: a = 2, b = 3
Output: 5

```

 

**Constraints:**

	- `-1000 <= a, b <= 1000`

## Solution

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

## 思路

- **位元運算：** `a ^ b` = 無進位和，`(a & b) << 1` = 進位。重複：新 a = 無進位和，新 b = 進位，直到 b 為 0。Python 整數為任意精度，需用 32 位遮罩與補數處理負數。

## 時間 / 空間複雜度

- **時間:** O(1)（位元數固定）。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Bit Manipulation、Full Adder、補數表示
