# Same Tree

**Topic:** Tree

- **LeetCode:** [100. Same Tree](https://leetcode.com/problems/same-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```

Input: p = [1,2,3], q = [1,2,3]
Output: true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```

Input: p = [1,2], q = [1,null,2]
Output: false

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```

Input: p = [1,2,1], q = [1,1,2]
Output: false

```

 

**Constraints:**

	- The number of nodes in both trees is in the range `[0, 100]`.

	- `-10^4 <= Node.val <= 10^4`

## Solution

```python
# LeetCode 100. Same Tree
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """兩樹相同：結構與數值都相同。遞迴比較根與左右子樹。"""
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

```

## 思路

- **遞迴：** 兩者皆空則 True；一空一非空或值不同則 False；否則遞迴比較左子樹與右子樹。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h)。

## 相關閱讀

- **資料結構:** Binary Tree、遞迴
