# Implement Trie (Prefix Tree)

- **LeetCode:** [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

	- `Trie()` Initializes the trie object.

	- `void insert(String word)` Inserts the string `word` into the trie.

	- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.

	- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

 

**Example 1:**

```

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

```

 

**Constraints:**

	- `1 <= word.length, prefix.length <= 2000`

	- `word` and `prefix` consist only of lowercase English letters.

	- At most `3 * 10^4` calls **in total** will be made to `insert`, `search`, and `startsWith`.

## Solution

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

## 思路

- **多叉樹：** 每個節點有 children（字元→子節點）與 is_end。insert 沿路建節點並在結尾標記；search 走到底看 is_end；startsWith 走完 prefix 即 True。

## 時間 / 空間複雜度

- **時間:** 單次操作 O(m)，m 為單詞/前綴長度。
- **空間:** O(總字元數)。

## 相關閱讀

- **資料結構:** Trie、Prefix Tree
- **演算法:** 字串集合、前綴匹配
