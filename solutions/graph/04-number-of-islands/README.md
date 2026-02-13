# Number of Islands

- **LeetCode:** [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

網格中 '1' 為陸地、'0' 為水，上下左右相連的 '1' 為一座島，求島嶼數量。

## 思路

- **DFS/BFS：** 遍歷每個格子，遇到 '1' 就從該格做 DFS 把整座島標記成已訪（例如改為 '0'），島嶼數即發起 DFS 的次數。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(m×n)（遞迴棧最壞）。

## 相關閱讀

- **演算法:** DFS、BFS、Connected Components
