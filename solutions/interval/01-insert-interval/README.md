# Insert Interval

- **LeetCode:** [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

給定已按起點排序且無重疊的區間列表，插入一個新区間並合併所有重疊區間。

## 思路

- 左邊完全在 newInterval 前的直接加入；與 newInterval 有交集的區間合併成一個新区間；右邊完全在後的直接加入。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1) 額外（不含輸出）。

## 相關閱讀

- **演算法:** 區間合併、線性掃描
