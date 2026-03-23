# Binary Tree Maximum Path Sum

**Topic:** Binary Tree
- **LeetCode 連結:** [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- **難度:** Hard

## 題目描述

給定一棵二元樹，路徑可以從任意節點出發到任意節點（不必經過根）。求路徑上節點值之和的最大值。節點值可能為負數。

## 解題思路

1. 定義遞迴函式，回傳以當前節點為端點的最大單邊路徑和。
2. 遞迴計算左、右子樹的最大增益（若為負則取 0，即不選）。
3. 以「左增益 + 節點值 + 右增益」更新全域最大路徑和（經過當前節點的完整路徑）。
4. 回傳「節點值 + max(左增益, 右增益)」給上層使用。

## 程式碼

```python
# LeetCode 124. Binary Tree Maximum Path Sum
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        路徑為任意節點到任意節點（可經由根）。遞迴回傳「以該節點為端點」的最大單邊路徑和，並用「左+根+右」更新全域最大。
        """
        self.best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return self.best
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(h)。
