# Best Time to Buy and Sell Stock

**Topic:** Array
- **LeetCode 連結:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **難度:** Easy

## 題目描述

給定一個整數陣列 `prices`，其中 `prices[i]` 代表第 `i` 天的股票價格。你只能選擇某一天買入、之後某一天賣出，求能獲得的最大利潤。若無法獲利則回傳 0。

## 解題思路

1. 初始化「至今最低價」為第一天的價格，「最大利潤」為 0。
2. 從左到右遍歷每一天的價格。
3. 計算若今天賣出的利潤（今天價格 - 至今最低價），更新最大利潤。
4. 更新「至今最低價」為目前遇過的最小值。
5. 遍歷結束後回傳最大利潤。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
