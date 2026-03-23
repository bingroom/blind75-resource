# Combination Sum IV

**Topic:** Dynamic Programming
- **LeetCode 連結:** [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
- **難度:** Medium

## 題目描述

給定一個不重複的正整數陣列和目標值 target，計算從陣列中選數（可重複使用）湊出目標值的組合數。不同順序算不同組合。

## 解題思路

1. 建立 dp 陣列，dp[i] 表示湊出數值 i 的組合數。
2. 初始化 dp[0] = 1。
3. 對每個值 i 從 1 到 target，遍歷陣列中的每個數字 x，若 i >= x 則 dp[i] += dp[i-x]。
4. 回傳 dp[target]。

## 程式碼

```python
# LeetCode 377. Combination Sum IV (順序不同算不同)
# 時間複雜度: O(target * n)  空間複雜度: O(target)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        用 nums 中的數（可重複）湊出 target，順序不同算不同組合，求組合數。dp[i] = 湊出 i 的組合數。
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    dp[i] += dp[i - x]
        return dp[target]
```

## 複雜度分析

- **時間複雜度:** O(target × n)。
- **空間複雜度:** O(target)。
