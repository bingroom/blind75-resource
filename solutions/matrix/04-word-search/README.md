# Word Search

- **LeetCode:** [79. Word Search](https://leetcode.com/problems/word-search/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

在二維字元網格中，找是否存在相鄰（上下左右）格子可依序組成給定單詞（每個格子最多用一次）。

## 思路

- **DFS + 回溯：** 從每個格子出發嘗試匹配 word，用過格暫時標記（如改為 '#'），遞迴後還原，以便其他路徑使用。

## 時間 / 空間複雜度

- **時間:** O(m×n×4^L)，L 為 word 長度。
- **空間:** O(L) 遞迴棧。

## 相關閱讀

- **演算法:** DFS、Backtracking
