# Add and Search Word

- **LeetCode:** [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

實作 addWord(word) 與 search(word)，其中 search 的 word 可含 '.' 表示任意一個字元。

## 思路

- **Trie + 遞迴搜尋：** 用 Trie 存單詞。search 時若遇到 '.' 則枚舉所有子節點遞迴；否則照一般 Trie 走。

## 時間 / 空間複雜度

- **時間:** 插入 O(m)；查詢無 '.' 為 O(m)，有 '.' 最壞 O(26^m)。
- **空間:** O(n·m)。

## 相關閱讀

- **資料結構:** Trie、遞迴搜尋
