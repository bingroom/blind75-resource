# Invert Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- **難度:** Easy

## 題目描述

給定一棵二元樹的根節點，將整棵樹左右翻轉（鏡像反轉），回傳翻轉後的根節點。每個節點的左右子樹互相交換。

## 解題思路

1. 若根節點為空，直接回傳 `None`。
2. 交換當前節點的左右子節點。
3. 遞迴地對左子樹和右子樹執行相同操作。
4. 回傳根節點。

## 程式碼

```python
# LeetCode 226. Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """左右子樹交換後，遞迴反轉左右子樹。"""
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(h)。
