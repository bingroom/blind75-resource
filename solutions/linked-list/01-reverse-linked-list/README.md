# Reverse Linked List

- **LeetCode:** [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

反轉單向鏈表（in-place，O(1) 額外空間）。

## 思路

- **迭代：** prev = None，每次把當前節點的 next 改為 prev，再 prev=cur、cur=原 next，直到 cur 為 None，回傳 prev。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **資料結構:** Linked List、指針操作
