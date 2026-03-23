# Best Time to Buy and Sell Stock

**Topic:** Array

- **LeetCode:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

 

**Example 1:**

```

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

**Example 2:**

```

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

```

 

**Constraints:**

	- `1 <= prices.length <= 10^5`

	- `0 <= prices[i] <= 10^4`

## Solution

```python
# LeetCode 121. Best Time to Buy and Sell Stock
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        只能買一次、賣一次。在最低價之後找最高價賣出。
        維護「至今最低價」與「至今最大利潤」，一次遍歷更新。
        """
        if not prices:
            return 0
        # 至今遇到的最低買入價
        min_price = prices[0]
        # 至今能得到的最大利潤
        max_profit = 0
        for p in prices:
            # 若今天賣出，利潤 = 今天價格 - 至今最低價
            max_profit = max(max_profit, p - min_price)
            # 更新「至今最低價」（買入日可選今天）
            min_price = min(min_price, p)
        return max_profit

```

## 思路

- 對每個「賣出日」，最優買入日一定是該日**之前**的最低價。
- 一次遍歷：維護 `min_price`（至今最低價）與 `max_profit`（至今最大利潤），每到新的一天先算「今天賣出的利潤」更新 `max_profit`，再更新 `min_price`。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** 貪心 (Greedy)、單遍歷 (one-pass)
