# Lowest Common Ancestor of a BST

- **LeetCode:** [235. Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

在 BST 中求 p、q 兩節點的最近共同祖先（LCA）。

## 思路

- **BST 性質：** 若 p、q 都小於根則 LCA 在左子樹；都大於根則在右子樹；否則根即為 LCA。可迭代或遞迴。

## 時間 / 空間複雜度

- **時間:** O(h)。
- **空間:** O(1) 迭代。

## 相關閱讀

- **資料結構:** BST、LCA
- **演算法:** 二元搜尋（在樹上）
