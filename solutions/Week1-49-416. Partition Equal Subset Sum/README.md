# Partition Equal Subset Sum

**Topic:** Dynamic Programming
- **LeetCode 連結:** [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- **難度:** Medium

## 題目描述

給定一個只含正整數的非空陣列，判斷是否能將該陣列分割為兩個子集，使得兩個子集的元素和相等。

## 解題思路

1. 計算陣列總和，若為奇數則無法均分，直接回傳 False。
2. 目標值 target 為總和的一半，轉化為 0/1 背包問題。
3. 建立布林陣列 dp，dp[j] 表示是否能用子集湊出和為 j。
4. 對每個數字，從 target 倒序遍歷更新 dp（倒序避免重複使用同一元素）。
5. 回傳 dp[target]。

## 程式碼

```python
# LeetCode 416. Partition Equal Subset Sum
# Time: O(n * target)  Space: O(target)

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        # dp[j] = True if we can form sum j using a subset of nums
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Traverse backwards to avoid using the same element twice (0/1 knapsack)
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
```

## 複雜度分析

- **時間複雜度:** O(n * target), where target = sum(nums) / 2
- **空間複雜度:** O(target)
