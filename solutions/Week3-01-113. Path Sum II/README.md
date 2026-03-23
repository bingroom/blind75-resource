# Path Sum II

**Topic:** Binary Tree
- **LeetCode 連結:** [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
- **難度:** Medium

## 題目描述

給定一棵二元樹和一個目標和，找出所有從根節點到葉節點的路徑，使路徑上的節點值之和等於目標和。

## 解題思路

1. 使用 DFS 回溯法，從根節點向下遍歷。
2. 每到一個節點，將其值加入當前路徑，並將剩餘目標和減去節點值。
3. 若到達葉節點且剩餘目標和恰好等於節點值，將當前路徑的副本加入結果。
4. 遞迴處理左右子樹後，回溯移除最後加入的節點。

## 程式碼

```python
# LeetCode 113. Path Sum II
# Time: O(n)  Space: O(h)

from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        """DFS backtracking: collect root-to-leaf paths that sum to target."""
        result: List[List[int]] = []

        def dfs(node: Optional[TreeNode], remaining: int, path: List[int]):
            if not node:
                return
            path.append(node.val)
            # Check if leaf with correct sum
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])  # copy current path
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)
            path.pop()  # backtrack

        dfs(root, targetSum, [])
        return result
```

## 複雜度分析

- **時間複雜度:** O(n) -- visit every node; copying paths costs O(h) each but bounded by O(n * h) total.
- **空間複雜度:** O(h) -- recursion stack and current path.
