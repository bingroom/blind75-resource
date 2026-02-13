# Word Search II

- **LeetCode:** [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

在二維網格中找所有在 words 中出現的單詞（相鄰、每格最多用一次），回傳列表。

## 思路

- **Trie + DFS 回溯：** 先將 words 建成 Trie。對網格每個格子做 DFS，沿 Trie 走；若走到某節點有單詞則加入答案並清掉該節點單詞（去重）；用過格標記後還原。

## 時間 / 空間複雜度

- **時間:** 建 Trie O(總長) + 網格 DFS。
- **空間:** O(單詞總長度)。

## 相關閱讀

- **資料結構:** Trie
- **演算法:** DFS、Backtracking、Word Search I 進階
