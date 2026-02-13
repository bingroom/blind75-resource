# Reorder List

- **LeetCode:** [143. Reorder List](https://leetcode.com/problems/reorder-list/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

將鏈表改為 L0 → Ln → L1 → Ln-1 → L2 → ...（頭尾交錯），要求 O(1) 空間。

## 思路

- **找中點**（快慢指針）→ **反轉後半段** → **兩段交錯合併**（前半與反轉後的後半一節一節接）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** 找中點、反轉鏈表、合併
