# Design Add and Search Words Data Structure

**Topic:** Trie
- **LeetCode 連結:** [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- **難度:** Medium

## 題目描述

設計一個資料結構，支援新增單字和搜尋單字。搜尋時 '.' 可以匹配任意一個字母。

## 解題思路

1. 使用字典樹（Trie）儲存所有單字，每個節點包含子節點字典和結束標記。
2. 新增單字時，逐字元沿著 Trie 建立節點。
3. 搜尋時逐字元匹配：遇到一般字元直接查找子節點。
4. 遇到 '.' 時遞迴嘗試所有子節點，任一路徑成功即回傳 true。

## 程式碼

```python
# LeetCode 211. Add and Search Word - Data structure design
# 時間複雜度: 插入 O(m) 查詢 O(m) 或 O(26^m) 含 '.'  空間複雜度: O(n*m)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def find(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == ".":
                return any(find(child, i + 1) for child in node.children.values())
            if c not in node.children:
                return False
            return find(node.children[c], i + 1)
        return find(self.root, 0)
```

## 複雜度分析

- **時間複雜度:** 插入 O(m)；查詢無 '.' 為 O(m)，有 '.' 最壞 O(26^m)。
- **空間複雜度:** O(n·m)。
