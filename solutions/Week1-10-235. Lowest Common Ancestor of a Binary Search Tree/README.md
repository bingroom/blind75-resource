# Lowest Common Ancestor of a Binary Search Tree

**Topic:** Binary Search Tree
- **LeetCode 連結:** [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- **難度:** Easy

## 題目描述

給定一棵二元搜尋樹（BST）及兩個節點 `p` 和 `q`，找出它們的最近公共祖先（LCA）。最近公共祖先是同時為 `p` 和 `q` 祖先的最深節點。

## 解題思路

1. 從根節點開始，利用 BST 的性質進行判斷。
2. 若 `p` 和 `q` 的值都小於當前節點，則 LCA 在左子樹，往左走。
3. 若 `p` 和 `q` 的值都大於當前節點，則 LCA 在右子樹，往右走。
4. 否則當前節點即為 LCA（`p` 和 `q` 分別在左右子樹，或其中一個就是當前節點）。

## 程式碼

```python
# LeetCode 235. Lowest Common Ancestor of a BST
# 時間複雜度: O(h)  空間複雜度: O(1) 迭代
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        BST 的 LCA：若 p、q 都小於根則在左子樹，都大於根則在右子樹，否則根即為 LCA。
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return root
```

## 複雜度分析

- **時間複雜度:** O(h)。
- **空間複雜度:** O(1) 迭代。
