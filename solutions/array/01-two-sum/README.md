# Two Sum

- **LeetCode:** [1. Two Sum](https://leetcode.com/problems/two-sum/)
- **NeetCode 練習:** [Blind 75 → Two Sum](https://neetcode.io/problems?list=blind75)

## 題意

給定整數陣列 `nums` 與目標 `target`，回傳「和為 target」的兩個數的**索引**（恰好一組解）。

## 思路

- 暴力：雙迴圈枚舉 (i, j)，時間 O(n²)。
- 優化：用 **Hash Map** 存「已見過的數 → 索引」。遍歷時檢查 `target - nums[i]` 是否在 map 裡，有則回傳 `[map[need], i]`。

## 時間 / 空間複雜度

- **時間:** O(n)，單次遍歷 + 查表 O(1)。
- **空間:** O(n)，最壞存 n 個數。

## 相關閱讀

- **資料結構:** Hash Table（雜湊表）
- **演算法:** 以空間換時間、一次遍歷 (one-pass)
