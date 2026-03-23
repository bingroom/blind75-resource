# 3Sum Closest

- **LeetCode:** [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

## Problem Description

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

## Approach

**Sort + Two Pointers:**

1. Sort the array.
2. Fix the first element by iterating index `i` from `0` to `n - 3`.
3. Use two pointers (`left = i + 1`, `right = n - 1`) to find the best pair:
   - Compute `total = nums[i] + nums[left] + nums[right]`.
   - Update `closest` if `|total - target|` improves.
   - If `total < target`, move `left` right to increase the sum; if `total > target`, move `right` left; if equal, return immediately.

## Complexity

- **Time:** O(n^2) -- sorting is O(n log n), then O(n) iterations each with an O(n) two-pointer scan.
- **Space:** O(1) -- ignoring the space used by sorting.
