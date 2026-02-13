# Kth Smallest Element in a BST

- **LeetCode:** [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求 BST 中第 k 小的元素（1-indexed）。

## 思路

- **中序遍歷：** BST 中序為遞增，依序數到第 k 個即為答案。可提前終止不必遍歷整棵樹（若 k 小則 O(k)）。

## 時間 / 空間複雜度

- **時間:** O(k) 到 O(n)。
- **空間:** O(h)。

## 相關閱讀

- **演算法:** Inorder Traversal、BST 性質
- **資料結構:** BST
