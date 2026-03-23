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
