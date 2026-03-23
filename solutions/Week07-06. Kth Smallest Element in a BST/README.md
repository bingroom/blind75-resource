# Kth Smallest Element in a BST

**Topic:** Tree

- **LeetCode:** [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the `root` of a binary search tree, and an integer `k`, return *the* `k^th` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```

Input: root = [3,1,4,null,2], k = 1
Output: 1

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

```

 

**Constraints:**

	- The number of nodes in the tree is `n`.

	- `1 <= k <= n <= 10^4`

	- `0 <= Node.val <= 10^4`

 

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## Solution

```python
# LeetCode 230. Kth Smallest Element in a BST
# 時間複雜度: O(k) 或 O(n) 中序  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """BST 中序為遞增序，第 k 個即第 k 小。中序遍歷到第 k 個即回傳。"""
        self.k = k
        self.ans = None

        def inorder(node: Optional[TreeNode]) -> None:
            if not node or self.ans is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.ans

```

## 思路

- **中序遍歷：** BST 中序為遞增，依序數到第 k 個即為答案。可提前終止不必遍歷整棵樹（若 k 小則 O(k)）。

## 時間 / 空間複雜度

- **時間:** O(k) 到 O(n)。
- **空間:** O(h)。

## 相關閱讀

- **演算法:** Inorder Traversal、BST 性質
- **資料結構:** BST
