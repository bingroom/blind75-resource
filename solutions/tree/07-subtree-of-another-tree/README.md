# Subtree of Another Tree

- **LeetCode:** [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of` subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

```

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

```

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

```

 

**Constraints:**

	- The number of nodes in the `root` tree is in the range `[1, 2000]`.

	- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.

	- `-10^4 <= root.val <= 10^4`

	- `-10^4 <= subRoot.val <= 10^4`

## Solution

```python
# LeetCode 572. Subtree of Another Tree
# 時間複雜度: O(m * n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

## 思路

- **枚舉根 + Same Tree：** 對 root 的每個節點當作「子樹根」，用 Same Tree 邏輯比較是否與 subRoot 相同；若有一處相同即 True。

## 時間 / 空間複雜度

- **時間:** O(m×n)，m、n 為兩樹節點數。
- **空間:** O(h)。

## 相關閱讀

- **演算法:** 樹同構、遞迴
