# Serialize and Deserialize Binary Tree

- **LeetCode:** [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

實作將二元樹序列化成字串，以及從字串反序列化回樹（格式自訂）。

## 思路

- **層序 (BFS)：** 序列化時層序輸出，空節點用 "null"，逗號分隔。反序列化時依序取節點接左右子（每節點對應兩個 token：左、右）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** BFS、序列化
- **資料結構:** Binary Tree、Queue
