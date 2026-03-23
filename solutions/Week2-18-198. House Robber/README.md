# House Robber

**Topic:** Dynamic Programming
- **LeetCode 連結:** [198. House Robber](https://leetcode.com/problems/house-robber/)
- **難度:** Medium

## 題目描述

一個小偷沿著一排房屋行竊，每間房屋內有一定金額。相鄰的房屋不能同時被偷（否則會觸發警報），求在不觸發警報的情況下能偷到的最大金額。

## 解題思路

1. 定義 dp[i] 為考慮前 i 間房屋時的最大金額。
2. 對每間房屋有兩種選擇：偷（nums[i] + dp[i-2]）或不偷（dp[i-1]）。
3. 取兩者的較大值作為 dp[i]。
4. 使用兩個變數滾動更新，將空間優化至 O(1)。

## 程式碼

```python
# LeetCode 198. House Robber
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        相鄰不能同時偷，求最大金額。dp[i] = 考慮前 i 間的最大值，偷 i 則加 nums[i]+dp[i-2]，不偷則 dp[i-1]。
        """
        if not nums:
            return 0
        prev, cur = 0, nums[0]
        for i in range(1, len(nums)):
            prev, cur = cur, max(cur, prev + nums[i])
        return cur
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
