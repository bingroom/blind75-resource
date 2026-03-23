# Move Zeroes

- **LeetCode:** [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## Problem Description

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

## Approach

Use a **two-pointer** technique:

1. Keep a `write` pointer starting at index 0.
2. Iterate with a `read` pointer. Whenever `nums[read]` is non-zero, swap it with `nums[write]` and advance `write`.
3. After the loop, all non-zero values are packed at the front in their original order, and all zeroes have been swapped to the back.

The swap-based approach avoids a second pass to fill zeroes.

## Complexity

- **Time:** O(n) -- single pass.
- **Space:** O(1) -- in-place swaps.
