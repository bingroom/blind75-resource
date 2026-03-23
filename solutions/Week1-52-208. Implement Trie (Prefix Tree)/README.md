# Implement Trie (Prefix Tree)

**Topic:** Trie
- **LeetCode 連結:** [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- **難度:** Medium

## 題目描述

實作一個字典樹（Trie，又稱前綴樹），支援三種操作：插入單詞（`insert`）、搜尋單詞是否存在（`search`）、以及檢查是否有以指定前綴開頭的單詞（`startsWith`）。

## 解題思路

1. 每個 Trie 節點包含一個 `children` 雜湊表（字元 -> 子節點）和一個 `is_end` 布林標記。
2. `insert`：沿著單詞的每個字元依序走訪或建立子節點，最後標記結尾。
3. `search`：沿著單詞的每個字元走訪子節點，若中途找不到則回傳 `False`；走完後檢查 `is_end` 是否為 `True`。
4. `startsWith`：與 `search` 類似，但走完前綴後不需檢查 `is_end`，直接回傳 `True`。

## 程式碼

```python
# LeetCode 208. Implement Trie (Prefix Tree)
# 時間複雜度: O(m) 插入/查詢  m=單詞長  空間複雜度: O(n * m)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
```

## 複雜度分析

- **時間複雜度:** 單次操作 O(m)，m 為單詞/前綴長度。
- **空間複雜度:** O(總字元數)。
