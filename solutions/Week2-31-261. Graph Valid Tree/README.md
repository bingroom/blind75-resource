# Graph Valid Tree

**Topic:** Graph
- **LeetCode 連結:** [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
- **難度:** Medium

## 題目描述

給定 n 個節點和一組邊，判斷這些邊是否構成一棵有效的樹。有效的樹必須是連通的且沒有環。

## 解題思路

1. 首先檢查邊數是否恰好為 n-1（樹的必要條件）。
2. 使用 Union-Find（並查集）資料結構。
3. 遍歷每條邊，將兩端點合併。
4. 若兩端點已在同一集合中，代表有環，回傳 false。
5. 所有邊處理完且無環，則為有效的樹。

## 程式碼

```python
# LeetCode 261. Graph Valid Tree
# Time: O(n * alpha(n))  Space: O(n)
# Union-Find approach

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree has exactly n-1 edges and no cycles
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # cycle detected
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True
```

## 複雜度分析

- **時間複雜度:** O(n * alpha(n)) where alpha is the inverse Ackermann function.
- **空間複雜度:** O(n) -- parent and rank arrays.
