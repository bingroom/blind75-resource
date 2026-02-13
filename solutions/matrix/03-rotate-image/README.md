# Rotate Image

- **LeetCode:** [48. Rotate Image](https://leetcode.com/problems/rotate-image/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

將 n×n 矩陣**順時針旋轉 90 度**，in-place。

## 思路

- **轉置 + 左右翻轉：** 先沿主對角線反轉（轉置），再對每一行做左右反轉，即得順時針 90 度。

## 時間 / 空間複雜度

- **時間:** O(n²)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** 矩陣變換、轉置
