# Binary Tree Right Side View

**Topic:** Binary Tree
- **LeetCode 連結:** [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- **難度:** Medium

## 題目描述

給定一棵二元樹的根節點，想像自己站在樹的右側，回傳從上到下每一層能看到的節點值（即每層最右邊的節點）。

## 解題思路

1. 使用 BFS 進行層序遍歷，以佇列儲存每一層的節點。
2. 對每一層，記錄該層的節點數量。
3. 遍歷該層所有節點，將左右子節點加入佇列。
4. 取每層的最後一個節點值加入結果陣列。

## 程式碼

```python
# LeetCode 199. Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS level order -- take the last node of each level."""
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node visited once.
- **空間複雜度:** O(n) -- queue can hold up to n/2 nodes at the widest level.
