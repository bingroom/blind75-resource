# House Robber

- **LeetCode:** [198. House Robber](https://leetcode.com/problems/house-robber/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

一排房子各有金額，不能偷相鄰兩間，求可偷到的最大總金額。

## 思路

- **DP：** 到第 i 間的最大值 = max(偷 i：nums[i]+前 i-2 的最大, 不偷 i：前 i-1 的最大)。可壓成兩變數 prev, cur。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Dynamic Programming、線性 DP
