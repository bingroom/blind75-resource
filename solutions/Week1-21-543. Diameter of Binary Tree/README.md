# Diameter of Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- **難度:** Easy

## 題目描述

給定一棵二元樹的根節點，回傳該樹的直徑。二元樹的直徑是指任意兩個節點之間最長路徑的邊數，該路徑不一定經過根節點。

## 解題思路

1. 使用遞迴由下而上計算每個節點的高度。
2. 對每個節點，經過它的最長路徑等於左子樹高度加右子樹高度。
3. 用全域變數記錄遍歷過程中遇到的最大直徑。
4. 每個節點回傳 1 + max(左高, 右高) 作為該子樹的高度。

## 程式碼

```python
# LeetCode 543. Diameter of Binary Tree
# Time: O(n)  Space: O(h)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Track max diameter while computing heights bottom-up."""
        self.ans = 0

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            # Diameter through this node = left + right
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        height(root)
        return self.ans
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node visited once.
- **空間複雜度:** O(h) -- recursion stack.
