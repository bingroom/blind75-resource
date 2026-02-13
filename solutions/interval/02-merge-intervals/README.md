# Merge Intervals

- **LeetCode:** [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

合併所有重疊的區間，回傳不重疊的區間列表。

## 思路

- **排序 + 線性掃描：** 按區間起點排序，遍歷時若當前區間與結果中最後一個重疊則合併（更新右端），否則加入新區間。

## 時間 / 空間複雜度

- **時間:** O(n log n)。
- **空間:** O(1) 額外（不含輸出）。

## 相關閱讀

- **演算法:** 區間排序、合併
