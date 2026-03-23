# Serialize and Deserialize Binary Tree

**Topic:** Binary Tree
- **LeetCode 連結:** [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- **難度:** Hard

## 題目描述

設計一個演算法，將二元樹序列化為字串，並能從該字串反序列化還原出原始的二元樹結構。序列化與反序列化的方式不限，只要能正確還原即可。

## 解題思路

1. 序列化：使用 BFS 層序遍歷，將節點值依序加入字串，空節點以 "null" 表示，用逗號分隔。
2. 反序列化：將字串以逗號分割，建立根節點並放入佇列。
3. 依序從佇列取出節點，讀取下兩個元素分別作為左子節點和右子節點。
4. 若元素不為 "null"，建立節點並加入佇列，直到所有元素處理完畢。

## 程式碼

```python
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
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(n)。
