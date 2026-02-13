# Clone Graph

- **LeetCode:** [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

深拷貝給定的無向圖（每個節點有 val 與 neighbors 列表）。

## 思路

- **BFS/DFS + Hash Map：** 用 map 存「原節點 → 新節點」。遍歷時若鄰居尚未建立則建立並入隊，並把新節點的 neighbors 接上對應的新節點。

## 時間 / 空間複雜度

- **時間:** O(V+E)。
- **空間:** O(V)。

## 相關閱讀

- **演算法:** BFS、Graph Traversal、Hash Map
