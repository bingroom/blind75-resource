# House Robber II

- **LeetCode:** [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

房子排成**環**，相鄰不能偷，求最大金額。

## 思路

- 環狀可拆成兩種線性：**不偷第一間**（考慮 nums[1:]）、**不偷最後一間**（考慮 nums[:-1]）。分別做 House Robber I，取較大值。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** DP、環狀拆成線性
