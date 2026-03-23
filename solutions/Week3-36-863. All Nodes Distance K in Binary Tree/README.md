# All Nodes Distance K in Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
- **難度:** Medium

## 題目描述

給定一棵二元樹、一個目標節點和距離 k，找出所有與目標節點距離為 k 的節點值。

## 解題思路

1. 先用 DFS 記錄每個節點的父節點，將樹轉為無向圖。
2. 從目標節點開始 BFS。
3. 每層向左子、右子和父節點擴展，記錄已訪問節點避免重複。
4. 當 BFS 到達第 k 層時，回傳該層所有節點的值。

## 程式碼

```python
# LeetCode 863. All Nodes Distance K in Binary Tree
# Time: O(n)  Space: O(n)

from collections import deque
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(
        self, root: TreeNode, target: TreeNode, k: int
    ) -> List[int]:
        """
        Convert tree to undirected graph via parent pointers,
        then BFS from target to find all nodes at distance k.
        """
        # Step 1: Record parent of every node using DFS
        parent = {}

        def dfs(node, par=None):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        # Step 2: BFS from target node
        visited = {target}
        queue = deque([target])
        dist = 0

        while queue:
            if dist == k:
                return [node.val for node in queue]
            dist += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return []
```

## 複雜度分析

- **時間複雜度:** O(n) -- DFS to build parent map + BFS visits each node at most once.
- **空間複雜度:** O(n) -- parent map, visited set, and BFS queue.
