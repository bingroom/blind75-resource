# Lowest Common Ancestor of a Binary Search Tree

**Topic:** Tree

- **LeetCode:** [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

```

**Example 3:**

```

Input: root = [2,1], p = 2, q = 1
Output: 2

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[2, 10^5]`.

	- `-10^9 <= Node.val <= 10^9`

	- All `Node.val` are **unique**.

	- `p != q`

	- `p` and `q` will exist in the BST.

## Solution

```python
# LeetCode 235. Lowest Common Ancestor of a BST
# 時間複雜度: O(h)  空間複雜度: O(1) 迭代
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


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

## 思路

- **BST 性質：** 若 p、q 都小於根則 LCA 在左子樹；都大於根則在右子樹；否則根即為 LCA。可迭代或遞迴。

## 時間 / 空間複雜度

- **時間:** O(h)。
- **空間:** O(1) 迭代。

## 相關閱讀

- **資料結構:** BST、LCA
- **演算法:** 二元搜尋（在樹上）
