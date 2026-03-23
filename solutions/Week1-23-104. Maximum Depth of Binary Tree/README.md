# Maximum Depth of Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- **難度:** Easy

## 題目描述

給定一棵二元樹，求其最大深度。最大深度是從根節點到最遠葉節點的最長路徑上的節點數。

## 解題思路

1. 若節點為空，回傳深度 0。
2. 遞迴計算左子樹和右子樹的最大深度。
3. 回傳 1 + max(左子樹深度, 右子樹深度)。

## 程式碼

```python
# LeetCode 104. Maximum Depth of Binary Tree
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """二元樹最大深度 = 1 + max(左深度, 右深度)，遞迴即可。"""
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(h) 遞迴棧。
