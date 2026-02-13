# Counting Bits

- **LeetCode:** [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

對每個 0 ≤ i ≤ n，回傳 i 的二進位中 1 的個數，組成陣列回傳。

## 思路

- **DP：** `ans[i] = ans[i >> 1] + (i & 1)`。即「右移一位的 1 的個數」加上「最低位是否為 1」。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1) 額外（不含輸出陣列）。

## 相關閱讀

- **演算法:** Dynamic Programming、Bit Manipulation
