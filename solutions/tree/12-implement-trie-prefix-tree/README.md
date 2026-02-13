# Implement Trie (Prefix Tree)

- **LeetCode:** [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

實作 Trie：insert(word)、search(word)、startsWith(prefix)。

## 思路

- **多叉樹：** 每個節點有 children（字元→子節點）與 is_end。insert 沿路建節點並在結尾標記；search 走到底看 is_end；startsWith 走完 prefix 即 True。

## 時間 / 空間複雜度

- **時間:** 單次操作 O(m)，m 為單詞/前綴長度。
- **空間:** O(總字元數)。

## 相關閱讀

- **資料結構:** Trie、Prefix Tree
- **演算法:** 字串集合、前綴匹配
