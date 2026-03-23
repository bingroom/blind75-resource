# Maximum Width of Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)
- **難度:** Medium

## 題目描述

給定一棵二元樹，求其最大寬度。寬度定義為某一層中最左和最右非空節點之間的距離（包含中間的空節點）。

## 解題思路

1. 使用 BFS 逐層遍歷，每個節點附帶一個位置索引。
2. 根節點索引為 0，左子節點索引為 2*idx，右子節點為 2*idx+1。
3. 每層開始時將索引正規化（減去該層第一個節點的索引），避免數值溢位。
4. 每層的寬度為最後一個索引 - 第一個索引 + 1，持續更新最大值。

## 程式碼

```python
# LeetCode 662. Maximum Width of Binary Tree
# Time: O(n)  Space: O(n)

from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """BFS with position indices; width = rightmost - leftmost + 1."""
        if not root:
            return 0
        max_width = 0
        queue = deque([(root, 0)])  # (node, index)
        while queue:
            level_size = len(queue)
            _, first_idx = queue[0]
            for _ in range(level_size):
                node, idx = queue.popleft()
                # Normalize index to prevent overflow
                idx -= first_idx
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
            # After processing level, last idx seen is the rightmost
            max_width = max(max_width, idx + 1)
        return max_width
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node visited once.
- **空間複雜度:** O(n) -- queue can hold up to n/2 nodes.
