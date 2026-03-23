# Coin Change

- **LeetCode:** [322. Coin Change](https://leetcode.com/problems/coin-change/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

 

**Example 1:**

```

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

```

**Example 2:**

```

Input: coins = [2], amount = 3
Output: -1

```

**Example 3:**

```

Input: coins = [1], amount = 0
Output: 0

```

 

**Constraints:**

	- `1 <= coins.length <= 12`

	- `1 <= coins[i] <= 2^31 - 1`

	- `0 <= amount <= 10^4`

## Solution

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

## 思路

- **DP：** `dp[i]` = 湊出金額 i 的最少硬幣數。對每個 i 枚舉「最後一枚硬幣」c，`dp[i] = min(dp[i], dp[i-c] + 1)`。

## 時間 / 空間複雜度

- **時間:** O(amount × |coins|)。
- **空間:** O(amount)。

## 相關閱讀

- **演算法:** Dynamic Programming、Unbounded Knapsack 型
