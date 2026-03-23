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
