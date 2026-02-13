# Longest Increasing Subsequence

- **LeetCode:** [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求陣列中最長**嚴格遞增**子序列的長度（不必連續）。

## 思路

- **DP + 二分：** 維護 `tails[i]` = 長度為 i+1 的遞增子序列的「最小結尾值」。遍歷 x 時用二分找第一個 ≥ x 的位置，替換或追加，最後 len(tails) 即為答案。

## 時間 / 空間複雜度

- **時間:** O(n log n)。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** DP、Binary Search、Patience Sorting
