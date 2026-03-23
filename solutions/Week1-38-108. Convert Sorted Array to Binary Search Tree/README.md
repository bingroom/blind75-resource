# Convert Sorted Array to Binary Search Tree

**Topic:** Binary Search Tree
- **LeetCode 連結:** [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
- **難度:** Easy

## 題目描述

給定一個升序排列的整數陣列，將其轉換為一棵高度平衡的二元搜尋樹。

## 解題思路

1. 選取陣列中間元素作為根節點，確保左右子樹高度差不超過 1。
2. 遞迴處理左半部分建立左子樹。
3. 遞迴處理右半部分建立右子樹。

## 程式碼

```python
# LeetCode 108. Convert Sorted Array to Binary Search Tree
# Time: O(n)  Space: O(log n)

from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Pick the middle element as root to ensure height balance."""

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)
```

## 複雜度分析

- **時間複雜度:** O(n) -- each element visited once.
- **空間複雜度:** O(log n) -- recursion stack for a balanced tree.
