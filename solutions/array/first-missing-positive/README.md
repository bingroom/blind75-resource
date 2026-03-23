# First Missing Positive

- **LeetCode:** [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

## Problem Description

Given an unsorted integer array `nums`, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

## Approach

**Index marking (cyclic sort):**

1. The answer is always in the range `[1, n + 1]` where `n` is the array length (by pigeonhole).
2. For each element, if its value `v` is in `[1, n]`, swap it to index `v - 1` (its "home" position). Repeat the swap at the current index until the current value is out of range or already in its correct spot.
3. After the placement pass, scan left to right. The first index `i` where `nums[i] != i + 1` means `i + 1` is missing.
4. If all positions are correct, return `n + 1`.

Each element is swapped at most once into its correct position, so the inner while loop runs O(n) total across all iterations.

## Complexity

- **Time:** O(n) -- each element moves to its final position at most once.
- **Space:** O(1) -- rearrangement is done in-place.
