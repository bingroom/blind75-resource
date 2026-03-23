# Binary Tree Level Order Traversal

**Topic:** Binary Tree
- **LeetCode 連結:** [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- **難度:** Medium

## 題目描述

給定一棵二元樹的根節點，回傳其節點值的層序遍歷結果（逐層由左到右）。結果以二維陣列表示，每一層為一個子陣列。

## 解題思路

1. 若根節點為空，回傳空陣列。
2. 使用佇列（deque）進行 BFS，初始將根節點加入佇列。
3. 每次處理一整層：記錄當前佇列長度，依序取出該層所有節點的值，並將子節點加入佇列。
4. 將每層的值列表加入結果，重複直到佇列為空。

## 程式碼

```python
# LeetCode 102. Binary Tree Level Order Traversal
# 時間複雜度: O(n)  空間複雜度: O(w) 最寬層
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(w)，w 為最寬層節點數。
