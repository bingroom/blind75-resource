# Coin Change

**Topic:** Dynamic Programming
- **LeetCode 連結:** [322. Coin Change](https://leetcode.com/problems/coin-change/)
- **難度:** Medium

## 題目描述

給定不同面額的硬幣陣列 `coins` 和一個目標金額 `amount`，求湊出該金額所需的最少硬幣數。每種硬幣可以無限使用。若無法湊出則回傳 -1。

## 解題思路

1. 建立 DP 陣列 `dp`，其中 `dp[i]` 代表湊出金額 `i` 所需的最少硬幣數，初始化為無限大，`dp[0] = 0`。
2. 對每個金額 `i` 從 1 到 `amount`，枚舉每種硬幣面額 `c`。
3. 若 `i >= c`，則 `dp[i] = min(dp[i], dp[i - c] + 1)`（選一枚面額 `c` 的硬幣）。
4. 最終若 `dp[amount]` 仍為無限大則回傳 -1，否則回傳 `dp[amount]`。

## 程式碼

```python
# LeetCode 322. Coin Change
# 時間複雜度: O(amount * len(coins))  空間複雜度: O(amount)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        用最少硬幣數湊出 amount，無法則 -1。dp[i] = 湊出 i 的最少硬幣數，枚舉最後一枚硬幣。
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
```

## 複雜度分析

- **時間複雜度:** O(amount × |coins|)。
- **空間複雜度:** O(amount)。
