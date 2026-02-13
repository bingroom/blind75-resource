# Construct Binary Tree from Preorder and Inorder Traversal

- **LeetCode:** [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

用前序與中序遍歷結果重建二元樹（假設值不重複）。

## 思路

- **遞迴：** 前序第一個為根；在中序中找到根的位置，左半為左子樹、右半為右子樹，對應前序中的連續區間，遞迴建左右子樹。用 map 存中序「值→索引」以 O(1) 找根位置。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)（map + 遞迴棧）。

## 相關閱讀

- **演算法:** 樹的遍歷、遞迴建樹
- **資料結構:** Binary Tree、Preorder、Inorder
