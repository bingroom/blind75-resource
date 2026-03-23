# Rotate Array

- **LeetCode:** [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps in-place.

## Approach

Use the **three-reverse** technique:

1. Normalize `k` with `k %= n` to handle cases where `k > n`.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the remaining `n - k` elements.

This works because reversing the whole array puts the last `k` elements at the front (but backwards), and the two partial reverses fix their internal order.

## Complexity

- **Time:** O(n) -- three passes, each at most O(n).
- **Space:** O(1) -- in-place swaps only.
