# LeetCode 133. Clone Graph
# 時間複雜度: O(V + E)  空間複雜度: O(V)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        深拷貝無向圖。用 dict 存 原節點 -> 新節點，BFS/DFS 遍歷並建立新節點與邊。
        """
        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val)
        from collections import deque
        q = deque([node])
        while q:
            u = q.popleft()
            for v in u.neighbors:
                if v not in clone:
                    clone[v] = Node(v.val)
                    q.append(v)
                clone[u].neighbors.append(clone[v])
        return clone[node]
