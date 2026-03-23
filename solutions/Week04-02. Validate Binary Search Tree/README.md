# Validate Binary Search Tree

**Topic:** Tree

- **LeetCode:** [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

	- The left subtree of a node contains only nodes with keys **strictly less than** the node's key.

	- The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.

	- Both the left and right subtrees must also be binary search trees.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```

Input: root = [2,1,3]
Output: true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^4]`.

	- `-2^31 <= Node.val <= 2^31 - 1`

## Solution

```python
# LeetCode 98. Validate Binary Search Tree
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

## 思路

- **遞迴 + 區間：** 遞迴時傳 (lo, hi)，當前節點需在 (lo, hi) 內，左子樹區間 (lo, node.val)、右子樹 (node.val, hi)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h)。

## 相關閱讀

- **資料結構:** Binary Search Tree、遞迴
