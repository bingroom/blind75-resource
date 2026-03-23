# Construct Binary Tree from Preorder and Inorder Traversal

**Topic:** Tree

- **LeetCode:** [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

```

**Example 2:**

```

Input: preorder = [-1], inorder = [-1]
Output: [-1]

```

 

**Constraints:**

	- `1 <= preorder.length <= 3000`

	- `inorder.length == preorder.length`

	- `-3000 <= preorder[i], inorder[i] <= 3000`

	- `preorder` and `inorder` consist of **unique** values.

	- Each value of `inorder` also appears in `preorder`.

	- `preorder` is **guaranteed** to be the preorder traversal of the tree.

	- `inorder` is **guaranteed** to be the inorder traversal of the tree.

## Solution

```python
# LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
# 時間複雜度: O(n)  空間複雜度: O(n) 用 map
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC
# 注意：TreeNode 由 LeetCode 環境提供，勿在此重複定義

from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        用前序與中序建樹。前序第一個為根；在中序裡找到根，左為左子樹、右為右子樹，遞迴建左右並接上。
        """
        idx = {v: i for i, v in enumerate(inorder)}

        def build(po_lo: int, po_hi: int, io_lo: int, io_hi: int) -> Optional[TreeNode]:
            if po_lo > po_hi:
                return None
            root = TreeNode(preorder[po_lo])  # LeetCode 提供的 TreeNode
            i = idx[root.val]
            left_size = i - io_lo
            root.left = build(po_lo + 1, po_lo + left_size, io_lo, i - 1)
            root.right = build(po_lo + left_size + 1, po_hi, i + 1, io_hi)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

```

## 思路

- **遞迴：** 前序第一個為根；在中序中找到根的位置，左半為左子樹、右半為右子樹，對應前序中的連續區間，遞迴建左右子樹。用 map 存中序「值→索引」以 O(1) 找根位置。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)（map + 遞迴棧）。

## 相關閱讀

- **演算法:** 樹的遍歷、遞迴建樹
- **資料結構:** Binary Tree、Preorder、Inorder
