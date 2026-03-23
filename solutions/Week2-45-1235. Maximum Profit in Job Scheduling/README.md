# Maximum Profit in Job Scheduling

**Topic:** Binary Search
- **LeetCode 連結:** [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
- **難度:** Hard

## 題目描述

給定 n 個工作的開始時間、結束時間和利潤，同一時間只能做一份工作。求在不重疊的前提下，能獲得的最大總利潤。

## 解題思路

1. 將所有工作按結束時間排序。
2. 定義 dp[i] 為考慮前 i 個工作時的最大利潤。
3. 對每個工作，用二分搜尋找到結束時間不超過該工作開始時間的最晚工作。
4. dp[i] = max(不做第 i 個工作的 dp[i-1], 做第 i 個工作的 dp[k] + profit_i)。

## 程式碼

```python
# LeetCode 1235. Maximum Profit in Job Scheduling
# Time: O(n log n)  Space: O(n)

from typing import List
import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        # dp[i] = max profit considering the first i jobs (sorted by end time)
        dp = [0] * (n + 1)
        ends = [j[1] for j in jobs]

        for i in range(1, n + 1):
            start_i = jobs[i - 1][0]
            profit_i = jobs[i - 1][2]

            # Find the latest job that ends <= start_i using binary search
            k = bisect.bisect_right(ends, start_i, 0, i - 1)

            # Either skip this job or take it
            dp[i] = max(dp[i - 1], dp[k] + profit_i)

        return dp[n]
```

## 複雜度分析

- **時間複雜度:** O(n log n) -- sorting + binary search per job
- **空間複雜度:** O(n)
