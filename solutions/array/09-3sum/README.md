# 3Sum

- **LeetCode:** [15. 3Sum](https://leetcode.com/problems/3sum/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

找出所有「和為 0」的三元組，且答案不可重複。

## 思路

- **排序**後，枚舉第一個數 `nums[i]`，在 `i+1..n-1` 用**雙指針**找兩數和 = `-nums[i]`（即 2Sum）。重複的數用「與前一個相同就跳過」來去重。

## 時間 / 空間複雜度

- **時間:** O(n²)（排序 O(n log n) + 枚舉 O(n) × 雙指針 O(n)）。
- **空間:** O(1) 額外（不含輸出；排序可能 O(log n) 遞迴棧）。

## 相關閱讀

- **演算法:** Two Pointers、2Sum 變型、排序
