# Validate Binary Search Tree

- **LeetCode:** [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

判斷二元樹是否為有效的 BST（左 < 根 < 右，且整棵子樹都滿足）。

## 思路

- **遞迴 + 區間：** 遞迴時傳 (lo, hi)，當前節點需在 (lo, hi) 內，左子樹區間 (lo, node.val)、右子樹 (node.val, hi)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h)。

## 相關閱讀

- **資料結構:** Binary Search Tree、遞迴
