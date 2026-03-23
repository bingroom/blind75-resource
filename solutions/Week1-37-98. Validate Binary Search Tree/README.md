# Validate Binary Search Tree

**Topic:** Binary Search Tree
- **LeetCode 連結:** [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- **難度:** Medium

## 題目描述

給定一棵二元樹的根節點，判斷它是否為合法的二元搜尋樹（BST）。合法的 BST 要求左子樹所有節點值小於根節點，右子樹所有節點值大於根節點，且左右子樹本身也是合法的 BST。

## 解題思路

1. 使用遞迴，對每個節點傳遞允許的數值範圍 (lo, hi)。
2. 根節點的範圍為 (-inf, +inf)，每次往左子樹遞迴時上界改為當前節點值，往右子樹遞迴時下界改為當前節點值。
3. 若節點值不在範圍內，回傳 False；若所有節點皆合法，回傳 True。

## 程式碼

```python
# LeetCode 98. Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """BST：左子樹所有值 < 根 < 右子樹所有值。遞迴時傳遞 (min, max) 區間。"""
        def ok(node: Optional[TreeNode], lo: float, hi: float) -> bool:
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return ok(node.left, lo, node.val) and ok(node.right, node.val, hi)
        return ok(root, float("-inf"), float("inf"))
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(h)。
