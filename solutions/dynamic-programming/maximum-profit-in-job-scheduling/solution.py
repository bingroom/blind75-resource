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
