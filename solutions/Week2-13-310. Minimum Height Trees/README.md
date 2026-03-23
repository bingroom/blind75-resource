# Minimum Height Trees

**Topic:** Graph
- **LeetCode 連結:** [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)
- **難度:** Medium

## 題目描述

給定一棵有 n 個節點的無向樹，找出以哪些節點為根時樹的高度最小，回傳這些節點的編號。結果最多包含兩個節點。

## 解題思路

1. 建立鄰接表並找出所有葉節點（度數為 1 的節點）。
2. 從外層葉節點逐層向內剝離，類似拓撲排序。
3. 每次移除當前所有葉節點，更新鄰居的度數，產生新的葉節點。
4. 重複直到剩餘節點數不超過 2，這些即為最小高度樹的根。

## 程式碼

```python
# LeetCode 310. Minimum Height Trees
# Time: O(n)  Space: O(n)

from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Repeatedly trim leaf nodes layer by layer.
        The last 1 or 2 remaining nodes are the MHT roots.
        """
        if n <= 2:
            return list(range(n))

        # Build adjacency list
        neighbors = [set() for _ in range(n)]
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        # Initialize leaves (degree 1)
        leaves = deque(i for i in range(n) if len(neighbors[i]) == 1)
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                # Each leaf has exactly one neighbor
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node and edge processed once.
- **空間複雜度:** O(n) -- adjacency list and queue.
