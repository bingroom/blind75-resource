# Binary Tree Level Order Traversal

- **LeetCode:** [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

```

**Example 2:**

```

Input: root = [1]
Output: [[1]]

```

**Example 3:**

```

Input: root = []
Output: []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 2000]`.

	- `-1000 <= Node.val <= 1000`

## Solution

```python
# LeetCode 102. Binary Tree Level Order Traversal
# 時間複雜度: O(n)  空間複雜度: O(w) 最寬層
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """層序遍歷：BFS，每層一列表。"""
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level)
        return out

```

## 思路

- **BFS：** 用 queue，每次處理一層（依當前 queue 長度取出一層），將該層節點值放入列表，並把子節點入隊。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(w)，w 為最寬層節點數。

## 相關閱讀

- **演算法:** BFS、Level Order Traversal
- **資料結構:** Queue
