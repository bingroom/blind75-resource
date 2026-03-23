# Kth Smallest Element in a BST

**Topic:** Binary Search Tree
- **LeetCode 連結:** [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- **難度:** Medium

## 題目描述

給定一棵二元搜尋樹（BST）的根節點和一個整數 k，回傳樹中第 k 小的元素值。

## 解題思路

1. 利用 BST 的中序遍歷為遞增序列的特性。
2. 進行中序遍歷（左 -> 根 -> 右），每訪問一個節點就將計數器減 1。
3. 當計數器歸零時，當前節點即為第 k 小的元素，記錄答案並提前終止。

## 程式碼

```python
# LeetCode 230. Kth Smallest Element in a BST
# 時間複雜度: O(k) 或 O(n) 中序  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """BST 中序為遞增序，第 k 個即第 k 小。中序遍歷到第 k 個即回傳。"""
        self.k = k
        self.ans = None

        def inorder(node: Optional[TreeNode]) -> None:
            if not node or self.ans is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.ans
```

## 複雜度分析

- **時間複雜度:** O(k) 到 O(n)。
- **空間複雜度:** O(h)。
