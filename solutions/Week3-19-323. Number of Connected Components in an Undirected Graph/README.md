# Number of Connected Components in an Undirected Graph

**Topic:** Graph
- **LeetCode 連結:** [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- **難度:** Medium

## 題目描述

給定 n 個節點和一組無向邊，計算圖中連通分量的數量。

## 解題思路

1. 初始化並查集，每個節點為自己的父節點，連通分量數為 n。
2. 遍歷每條邊，對兩端點執行 union 操作。
3. 每次成功合併（兩端點不在同一集合），連通分量數減 1。
4. 回傳最終的連通分量數。

## 程式碼

```python
# LeetCode 323. Number of Connected Components in an Undirected Graph
# Time: O(n + E * alpha(n))  Space: O(n)
# Union-Find approach

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1

        return components
```

## 複雜度分析

- **時間複雜度:** O(n + E * alpha(n)) where E is the number of edges and alpha is the inverse Ackermann function.
- **空間複雜度:** O(n) -- parent and rank arrays.
