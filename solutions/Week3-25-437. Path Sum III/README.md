# Path Sum III

**Topic:** Binary Tree
- **LeetCode 連結:** [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
- **難度:** Medium

## 題目描述

給定一棵二元樹和目標和，計算樹中有多少條路徑的節點值總和等於目標和。路徑不需從根開始或在葉結束，但必須向下。

## 解題思路

1. 使用前綴和方法，DFS 遍歷樹。
2. 在每個節點計算從根到當前節點的累計和。
3. 查詢雜湊表中 (累計和 - 目標和) 出現的次數，即為以當前節點結尾的有效路徑數。
4. 回溯時從雜湊表移除當前前綴和，避免影響其他分支。

## 程式碼

```python
# LeetCode 437. Path Sum III
# Time: O(n)  Space: O(n)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Prefix sum approach: at each node, check how many previous
        prefix sums equal (current_sum - targetSum).
        """
        prefix_counts = {0: 1}  # base case: empty prefix
        self.count = 0

        def dfs(node: Optional[TreeNode], curr_sum: int):
            if not node:
                return
            curr_sum += node.val
            # Number of valid paths ending here
            self.count += prefix_counts.get(curr_sum - targetSum, 0)
            # Record current prefix sum
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            # Backtrack: remove current prefix sum when leaving this node
            prefix_counts[curr_sum] -= 1

        dfs(root, 0)
        return self.count
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node visited once.
- **空間複雜度:** O(n) -- prefix sum map and recursion stack.
