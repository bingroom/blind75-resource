# Reverse Bits

- **LeetCode:** [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

將給定的 32 位無符號整數的二進位表示反轉，回傳新的整數。

## 思路

- 從 n 的最低位開始取（n & 1），每次把結果左移並加上該位，共做 32 次。

## 時間 / 空間複雜度

- **時間:** O(1)（32 次）。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Bit Manipulation
