# Design In-Memory File System

**Topic:** Trie
- **LeetCode 連結:** [588. Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/)
- **難度:** Hard

## 題目描述

設計一個記憶體內的檔案系統，支援建立目錄、列出內容、建立檔案與讀取檔案等操作。

## 解題思路

1. 使用 Trie（前綴樹）結構表示目錄層級，每個節點包含子節點字典和檔案內容。
2. 實作路徑導航方法，沿路徑字串逐層找到對應節點。
3. ls 方法判斷是檔案還是目錄，分別回傳檔名或排序後的子項目列表。
4. mkdir、addContentToFile 和 readContentFromFile 透過路徑導航存取對應節點。

## 程式碼

```python
# LeetCode 588. Design In-Memory File System
# Time: O(m + n + k log k) for ls, O(m + n) for others  Space: O(total content)
# m = path length, n = content length, k = number of entries

from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.content = ""  # non-empty only for files
        self.is_file = False


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def _traverse(self, path: str) -> TrieNode:
        """Navigate to the node at the given path."""
        node = self.root
        if path == "/":
            return node
        for part in path.split("/")[1:]:  # skip empty string before first /
            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if node.is_file:
            # Return just the file name
            return [path.split("/")[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)  # defaultdict auto-creates nodes

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        return node.content
```

## 複雜度分析

- **時間複雜度:** O(m + k log k) for `ls` (m = path depth, k = entries to sort), O(m + n) for file operations (n = content length)
- **空間複雜度:** O(total stored content + total path nodes)
