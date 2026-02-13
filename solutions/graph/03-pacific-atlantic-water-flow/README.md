# Pacific Atlantic Water Flow

- **LeetCode:** [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

矩陣左與上為太平洋、右與下為大西洋，水只能從高往低（或同高）流。求能同時流到兩洋的格子座標。

## 思路

- **反向思考：** 從太平洋邊（第一行、第一列）與大西洋邊（最後一行、最後一列）分別做 DFS/BFS，標記「能流到該洋」的格子（從邊緣往高處走）。兩邊都能到的格子即為答案。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(m×n)。

## 相關閱讀

- **演算法:** DFS/BFS、多源點遍歷
