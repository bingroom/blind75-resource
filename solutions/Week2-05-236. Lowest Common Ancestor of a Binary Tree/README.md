# Lowest Common Ancestor of a Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- **難度:** Medium

## 題目描述

給定一棵二元樹和其中兩個節點 p 與 q，找出它們的最低共同祖先（LCA）。最低共同祖先是指同時為 p 和 q 的祖先中，深度最大的那個節點（節點本身也可以是自己的祖先）。

## 解題思路

1. 若當前節點為 None 或等於 p 或 q，直接回傳當前節點。
2. 分別遞迴搜尋左子樹和右子樹。
3. 若左右兩邊都回傳非空值，表示 p 和 q 分別在左右子樹中，當前節點即為 LCA。
4. 否則回傳非空的那一邊結果。

## 程式碼

```python
# LeetCode 236. Lowest Common Ancestor of a Binary Tree
# Time: O(n)  Space: O(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        If current node is p or q, return it.
        Recurse left and right. If both return non-null, current node is LCA.
        Otherwise return whichever side is non-null.
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

## 複雜度分析

- **時間複雜度:** O(n) -- worst case visits all nodes.
- **空間複雜度:** O(h) -- recursion stack.
