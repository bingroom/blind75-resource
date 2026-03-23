# Clone Graph

- **LeetCode:** [133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a reference of a node in a **connected** undirected graph.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```

class Node {
    public int val;
    public List<Node> neighbors;
}

```

 

**Test case format:**

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

**An adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

```

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

```

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

```

**Example 3:**

```

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

```

 

**Constraints:**

	- The number of nodes in the graph is in the range `[0, 100]`.

	- `1 <= Node.val <= 100`

	- `Node.val` is unique for each node.

	- There are no repeated edges and no self-loops in the graph.

	- The Graph is connected and all nodes can be visited starting from the given node.

## Solution

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

## 思路

- **BFS/DFS + Hash Map：** 用 map 存「原節點 → 新節點」。遍歷時若鄰居尚未建立則建立並入隊，並把新節點的 neighbors 接上對應的新節點。

## 時間 / 空間複雜度

- **時間:** O(V+E)。
- **空間:** O(V)。

## 相關閱讀

- **演算法:** BFS、Graph Traversal、Hash Map
