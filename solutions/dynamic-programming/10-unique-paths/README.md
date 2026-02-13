# Unique Paths

- **LeetCode:** [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

m×n 網格，從左上到右下只能向右或向下，求不同路徑數。

## 思路

- **DP：** dp[i][j] = 到 (i,j) 的路徑數 = dp[i-1][j] + dp[i][j-1]。可壓成一行，從左到右更新。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** Dynamic Programming、網格路徑計數
