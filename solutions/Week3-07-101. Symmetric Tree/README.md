# Symmetric Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
- **難度:** Easy

## 題目描述

給定一棵二元樹，判斷它是否為鏡像對稱的（左右子樹互為鏡像）。

## 解題思路

1. 定義遞迴輔助函式，同時比較兩個節點。
2. 若兩節點皆為空，回傳 True；若只有一個為空或值不同，回傳 False。
3. 遞迴檢查：左子樹的左子節點對應右子樹的右子節點，左子樹的右子節點對應右子樹的左子節點。

## 程式碼

```python
# LeetCode 101. Symmetric Tree
# Time: O(n)  Space: O(h)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check if left and right subtrees are mirror images."""

        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val
                and is_mirror(t1.left, t2.right)
                and is_mirror(t1.right, t2.left)
            )

        return is_mirror(root, root)
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node visited once.
- **空間複雜度:** O(h) -- recursion stack.
