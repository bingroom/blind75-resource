# Maximum Depth of Binary Tree

- **LeetCode:** [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求二元樹的最大深度（根到最遠葉的節點數）。

## 思路

- **遞迴：** 若為空回傳 0；否則 1 + max(左子樹深度, 右子樹深度)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h) 遞迴棧。

## 相關閱讀

- **資料結構:** Binary Tree、遞迴
