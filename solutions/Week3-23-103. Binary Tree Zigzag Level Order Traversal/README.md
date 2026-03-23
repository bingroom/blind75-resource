# Binary Tree Zigzag Level Order Traversal

**Topic:** Binary Tree
- **LeetCode 連結:** [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
- **難度:** Medium

## 題目描述

給定一棵二元樹，回傳其鋸齒形層序遍歷的結果（即第一層左到右，第二層右到左，交替進行）。

## 解題思路

1. 使用 BFS 進行層序遍歷。
2. 維護一個方向旗標，奇數層反轉該層結果。
3. 每層遍歷完畢後切換方向，將結果加入答案。

## 程式碼

```python
# LeetCode 103. Binary Tree Zigzag Level Order Traversal
# Time: O(n)  Space: O(n)

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """BFS level order; reverse odd-indexed levels."""
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right
        return result
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node visited once; reversing a level is O(level size).
- **空間複雜度:** O(n) -- queue and result storage.
