# Maximum Depth of Binary Tree

**Topic:** Tree

- **LeetCode:** [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```

Input: root = [3,9,20,null,null,15,7]
Output: 3

```

**Example 2:**

```

Input: root = [1,null,2]
Output: 2

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 10^4]`.

	- `-100 <= Node.val <= 100`

## Solution

```python
# LeetCode 104. Maximum Depth of Binary Tree
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """二元樹最大深度 = 1 + max(左深度, 右深度)，遞迴即可。"""
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

```

## 思路

- **遞迴：** 若為空回傳 0；否則 1 + max(左子樹深度, 右子樹深度)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h) 遞迴棧。

## 相關閱讀

- **資料結構:** Binary Tree、遞迴
