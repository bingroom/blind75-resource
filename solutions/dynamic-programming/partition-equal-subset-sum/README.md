# Partition Equal Subset Sum

- **LeetCode:** [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

## Problem Description

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or `false` otherwise.

## Approach

This is a classic 0/1 knapsack problem. If the total sum is odd, partitioning is impossible. Otherwise, the target is `total // 2` and we need to find a subset that sums to that target.

1. Compute the total sum. If odd, return `False`.
2. Set `target = total // 2`.
3. Use a 1D boolean DP array where `dp[j]` indicates whether sum `j` is achievable.
4. For each number, iterate backwards from `target` down to `num` to ensure each element is used at most once (0/1 knapsack property).
5. Return `dp[target]`.

## Complexity

- **Time:** O(n * target), where target = sum(nums) / 2
- **Space:** O(target)
