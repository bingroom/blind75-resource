# Combination Sum IV

- **LeetCode:** [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

用 nums 中的數（可重複）湊出 target，**順序不同視為不同組合**，求組合總數。

## 思路

- **DP：** `dp[i]` = 湊出 i 的組合數。對每個 i 枚舉「最後一個用的數字」x，dp[i] += dp[i-x]。注意先枚舉 i 再枚舉 x 才能計入不同順序。

## 時間 / 空間複雜度

- **時間:** O(target × n)。
- **空間:** O(target)。

## 相關閱讀

- **演算法:** Dynamic Programming、計數型 DP
