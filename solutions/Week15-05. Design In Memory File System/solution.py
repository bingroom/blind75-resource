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
