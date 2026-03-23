# LeetCode 297. Serialize and Deserialize Binary Tree
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC
# 注意：TreeNode 由 LeetCode 環境提供，勿在此重複定義

from typing import Optional
from collections import deque


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """用 BFS 層序，空節點用 'null'，逗號分隔。"""
        if not root:
            return ""
        q = deque([root])
        parts = []
        while q:
            node = q.popleft()
            if node is None:
                parts.append("null")
            else:
                parts.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(parts)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """依層序還原：用 queue 依序接左右子。"""
        if not data:
            return None
        parts = data.split(",")
        root = TreeNode(int(parts[0]))
        q = deque([root])
        i = 1
        while q and i < len(parts):
            node = q.popleft()
            if i < len(parts) and parts[i] != "null":
                node.left = TreeNode(int(parts[i]))
                q.append(node.left)
            i += 1
            if i < len(parts) and parts[i] != "null":
                node.right = TreeNode(int(parts[i]))
                q.append(node.right)
            i += 1
        return root
