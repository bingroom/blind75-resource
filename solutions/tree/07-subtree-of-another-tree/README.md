# Subtree of Another Tree

- **LeetCode:** [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

判斷 subRoot 是否為 root 的某棵**子樹**（連續且結構與數值完全相同）。

## 思路

- **枚舉根 + Same Tree：** 對 root 的每個節點當作「子樹根」，用 Same Tree 邏輯比較是否與 subRoot 相同；若有一處相同即 True。

## 時間 / 空間複雜度

- **時間:** O(m×n)，m、n 為兩樹節點數。
- **空間:** O(h)。

## 相關閱讀

- **演算法:** 樹同構、遞迴
