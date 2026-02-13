# Non-overlapping Intervals

- **LeetCode:** [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

移除最少數量的區間，使剩餘區間兩兩不重疊。求最少移除數。

## 思路

- **等價於「最多保留幾個不重疊區間」：** 按區間**右端**排序，貪心取：每次取與當前 end 不重疊且右端盡量小的區間。答案 = 總數 - 保留數。

## 時間 / 空間複雜度

- **時間:** O(n log n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Greedy、區間調度
