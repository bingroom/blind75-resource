# Binary Tree Level Order Traversal

- **LeetCode:** [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

回傳二元樹的層序遍歷結果（每層一個列表）。

## 思路

- **BFS：** 用 queue，每次處理一層（依當前 queue 長度取出一層），將該層節點值放入列表，並把子節點入隊。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(w)，w 為最寬層節點數。

## 相關閱讀

- **演算法:** BFS、Level Order Traversal
- **資料結構:** Queue
