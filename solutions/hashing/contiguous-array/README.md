# Contiguous Array

- **LeetCode:** [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)

## Problem Description

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

## Approach

1. Replace every 0 with -1. Now the problem is: find the longest subarray whose sum is 0.
2. Maintain a running prefix sum and a hash map that records the **first** index at which each prefix sum was seen.
3. Seed the map with `{0: -1}` so that a subarray starting from index 0 is handled.
4. At each index `i`, if the current prefix sum was seen before at index `j`, then the subarray `[j+1 .. i]` sums to 0 (equal 0s and 1s). Update the maximum length.
5. Only store the first occurrence of each sum to maximize the subarray length.

## Complexity

- **Time:** O(n) — single pass through the array.
- **Space:** O(n) — hash map stores at most n+1 distinct prefix sums.
