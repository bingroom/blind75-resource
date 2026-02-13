# Climbing Stairs

- **LeetCode:** [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

每次可爬 1 或 2 階，求到第 n 階有幾種不同方法。

## 思路

- **DP：** 到第 i 階的方法數 = 從 i-1 爬一步 + 從 i-2 爬兩步，即 `dp[i] = dp[i-1] + dp[i-2]`。可只保留前兩項，空間 O(1)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Dynamic Programming、Fibonacci 數列
