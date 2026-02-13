# Coin Change

- **LeetCode:** [322. Coin Change](https://leetcode.com/problems/coin-change/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

給硬幣面額與目標金額 amount，求湊出 amount 的**最少硬幣數**，無法湊出則回傳 -1。

## 思路

- **DP：** `dp[i]` = 湊出金額 i 的最少硬幣數。對每個 i 枚舉「最後一枚硬幣」c，`dp[i] = min(dp[i], dp[i-c] + 1)`。

## 時間 / 空間複雜度

- **時間:** O(amount × |coins|)。
- **空間:** O(amount)。

## 相關閱讀

- **演算法:** Dynamic Programming、Unbounded Knapsack 型
