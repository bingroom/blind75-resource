# Serialize and Deserialize Binary Tree

- **LeetCode:** [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

```

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

```

**Example 2:**

```

Input: root = []
Output: []

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 10^4]`.

	- `-1000 <= Node.val <= 1000`

## Solution

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

## 思路

- **層序 (BFS)：** 序列化時層序輸出，空節點用 "null"，逗號分隔。反序列化時依序取節點接左右子（每節點對應兩個 token：左、右）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** BFS、序列化
- **資料結構:** Binary Tree、Queue
