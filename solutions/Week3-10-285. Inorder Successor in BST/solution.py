# LeetCode 285. Inorder Successor in BST
# Time: O(h)  Space: O(1)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderSuccessor(
        self, root: Optional[TreeNode], p: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        BST property: successor is the smallest node larger than p.
        Go left when current val > p.val (potential successor),
        go right otherwise.
        """
        successor = None
        while root:
            if root.val > p.val:
                successor = root  # candidate; try to find a smaller one
                root = root.left
            else:
                root = root.right  # need a larger value
        return successor
