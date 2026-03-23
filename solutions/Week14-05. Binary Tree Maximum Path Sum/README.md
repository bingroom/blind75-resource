# Binary Tree Maximum Path Sum

**Topic:** Tree

- **LeetCode:** [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

```

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

```

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.

	- `-1000 <= Node.val <= 1000`

## Solution

```python
# LeetCode 124. Binary Tree Maximum Path Sum
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

## 思路

- **遞迴：** 定義「以該節點為端點」往下的最大單邊路徑和。對每個節點，用「左單邊 + 根 + 右單邊」更新全域最大；回傳值為根 + max(左, 右)（若子樹為負則取 0）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h)。

## 相關閱讀

- **演算法:** Tree DP、後序遍歷
