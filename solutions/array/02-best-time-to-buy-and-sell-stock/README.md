# Best Time to Buy and Sell Stock

- **LeetCode:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

給每日股價 `prices`，只能買一次、賣一次（且賣在買之後），求最大利潤。

## 思路

- 對每個「賣出日」，最優買入日一定是該日**之前**的最低價。
- 一次遍歷：維護 `min_price`（至今最低價）與 `max_profit`（至今最大利潤），每到新的一天先算「今天賣出的利潤」更新 `max_profit`，再更新 `min_price`。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** 貪心 (Greedy)、單遍歷 (one-pass)
