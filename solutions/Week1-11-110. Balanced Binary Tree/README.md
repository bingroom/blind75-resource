# Balanced Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- **難度:** Easy

## 題目描述

給定一棵二元樹，判斷它是否為高度平衡的二元樹。高度平衡指每個節點的左右子樹高度差不超過 1。

## 解題思路

1. 使用自底向上的遞迴方式，定義輔助函式回傳子樹高度。
2. 遞迴計算左子樹和右子樹的高度。
3. 若任一子樹不平衡（回傳 -1），或左右高度差超過 1，則回傳 -1 表示不平衡。
4. 否則回傳 `1 + max(左高度, 右高度)`；最終檢查根節點的回傳值是否為 -1。

## 程式碼

```python
# LeetCode 110. Balanced Binary Tree
# Time: O(n)  Space: O(h)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Bottom-up recursion: return height or -1 if unbalanced."""

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node visited once.
- **空間複雜度:** O(h) -- recursion stack, where h is tree height.
