# Subtree of Another Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- **難度:** Easy

## 題目描述

給定兩棵二元樹 root 和 subRoot，判斷 subRoot 是否為 root 的子樹（結構和值完全相同的子樹）。

## 解題思路

1. 對 root 的每個節點檢查是否與 subRoot 完全相同。
2. 使用輔助函式逐節點比較兩棵樹是否相同。
3. 若當前節點不匹配，遞迴檢查左子樹和右子樹。

## 程式碼

```python
# LeetCode 572. Subtree of Another Tree
# 時間複雜度: O(m * n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """判斷 subRoot 是否為 root 的某棵子樹。對 root 每個節點做 isSameTree(root, subRoot)。"""
        if not subRoot:
            return True
        if not root:
            return False
        if self._same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _same(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self._same(p.left, q.left) and self._same(p.right, q.right)
```

## 複雜度分析

- **時間複雜度:** O(m×n)，m、n 為兩樹節點數。
- **空間複雜度:** O(h)。
