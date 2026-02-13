# Longest Consecutive Sequence

- **LeetCode:** [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

在未排序整數陣列中，求最長**連續數字**序列的長度（例如 3,1,2,4 → 長度 4）。

## 思路

- **Set：** 將所有數放入 set。只從「序列起點」開始計數（即 x-1 不在 set 的 x），往右數到不在 set 為止，更新最長長度。這樣每數只被起點數一次，O(n)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Set、Hash Table
- **演算法:** 只從邊界擴展避免重複
