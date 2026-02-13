# Sum of Two Integers

- **LeetCode:** [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

在不使用 `+`、`-` 的前提下，計算兩整數之和。

## 思路

- **位元運算：** `a ^ b` = 無進位和，`(a & b) << 1` = 進位。重複：新 a = 無進位和，新 b = 進位，直到 b 為 0。Python 整數為任意精度，需用 32 位遮罩與補數處理負數。

## 時間 / 空間複雜度

- **時間:** O(1)（位元數固定）。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Bit Manipulation、Full Adder、補數表示
