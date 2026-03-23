# Invert Binary Tree

**Topic:** Tree

- **LeetCode:** [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the `root` of a binary tree, invert the tree, and return *its root*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```

Input: root = [2,1,3]
Output: [2,3,1]

```

**Example 3:**

```

Input: root = []
Output: []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 100]`.

	- `-100 <= Node.val <= 100`

## Solution

```python
# LeetCode 226. Invert Binary Tree
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """左右子樹交換後，遞迴反轉左右子樹。"""
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

```

## 思路

- **遞迴：** 交換根的左右子樹指標，再分別對左、右子樹做反轉。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h)。

## 相關閱讀

- **資料結構:** Binary Tree、遞迴
