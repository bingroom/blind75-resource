# Maximum Profit in Job Scheduling

- **LeetCode:** [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

## Problem Description

We have `n` jobs where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`. Return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

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
