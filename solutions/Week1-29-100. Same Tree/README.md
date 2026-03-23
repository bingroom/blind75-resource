# Same Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [100. Same Tree](https://leetcode.com/problems/same-tree/)
- **難度:** Easy

## 題目描述

給定兩棵二元樹，判斷它們是否結構相同且每個對應節點的值都相等。

## 解題思路

1. 若兩節點皆為空，回傳 True。
2. 若其中一個為空或值不同，回傳 False。
3. 遞迴比較左子樹與右子樹是否相同。

## 程式碼

```python
# LeetCode 100. Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """兩樹相同：結構與數值都相同。遞迴比較根與左右子樹。"""
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(h)。
