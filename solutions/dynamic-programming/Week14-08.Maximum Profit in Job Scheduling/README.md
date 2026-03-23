# Maximum Profit in Job Scheduling

- **LeetCode:** [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

## Problem Description

We have `n` jobs where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`. Return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.


## Solution

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

## Approach

Sort jobs by end time, then use DP with binary search.

1. Sort all jobs by their end time.
2. Define `dp[i]` as the maximum profit considering the first `i` jobs.
3. For each job `i`, use binary search to find the latest job `k` whose end time is at most `start_i`. This gives us the best compatible preceding state.
4. `dp[i] = max(dp[i-1], dp[k] + profit_i)` -- either skip this job or take it.
5. Return `dp[n]`.

## Complexity

- **Time:** O(n log n) -- sorting + binary search per job
- **Space:** O(n)
