# Clone Graph

**Topic:** Graph
- **LeetCode 連結:** [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- **難度:** Medium

## 題目描述

給定一個無向連通圖中某個節點的參考，回傳該圖的深拷貝（clone）。圖中每個節點包含一個值和一個鄰居列表。

## 解題思路

1. 使用雜湊表（dict）建立「原節點 -> 複製節點」的映射。
2. 從給定節點開始 BFS，建立其複製節點並加入佇列。
3. 遍歷每個節點的鄰居：若尚未複製則建立新節點並加入佇列。
4. 將複製的鄰居節點加入當前複製節點的鄰居列表，最後回傳起始節點的複製。

## 程式碼

```python
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
```

## 複雜度分析

- **時間複雜度:** O(V+E)。
- **空間複雜度:** O(V)。
