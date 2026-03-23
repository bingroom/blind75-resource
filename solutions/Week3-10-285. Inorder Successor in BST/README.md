# Inorder Successor in BST

**Topic:** Binary Search Tree
- **LeetCode 連結:** [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)
- **難度:** Medium

## 題目描述

給定一棵二元搜尋樹和其中一個節點 p，找出 p 的中序後繼節點（即中序遍歷中 p 的下一個節點）。

## 解題思路

1. 利用 BST 性質，從根節點開始遍歷。
2. 若當前節點值大於 p，記錄為候選後繼，往左子樹尋找更小的候選。
3. 若當前節點值小於等於 p，往右子樹尋找更大的值。
4. 遍歷結束後回傳候選後繼。

## 程式碼

```python
# LeetCode 285. Inorder Successor in BST
# Time: O(h)  Space: O(1)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderSuccessor(
        self, root: Optional[TreeNode], p: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        BST property: successor is the smallest node larger than p.
        Go left when current val > p.val (potential successor),
        go right otherwise.
        """
        successor = None
        while root:
            if root.val > p.val:
                successor = root  # candidate; try to find a smaller one
                root = root.left
            else:
                root = root.right  # need a larger value
        return successor
```

## 複雜度分析

- **時間複雜度:** O(h) -- single root-to-leaf traversal.
- **空間複雜度:** O(1) -- iterative, no extra space.
