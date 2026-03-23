# Find the Duplicate Number

- **LeetCode:** [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

## Problem Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, there is exactly one repeated number. Return this repeated number. You must solve it without modifying the array and using only constant extra space.

## Approach

Use **Floyd's Cycle Detection** (Tortoise and Hare):

1. Treat the array as a linked list where index `i` points to `nums[i]`. Since values are in `[1, n]` and there are `n + 1` slots, a cycle is guaranteed, and the duplicate value is the cycle's entrance.
2. **Phase 1 -- Find intersection:** Move `slow` one step and `fast` two steps until they meet inside the cycle.
3. **Phase 2 -- Find entrance:** Reset `slow` to the start. Move both pointers one step at a time. Where they meet is the duplicate.

## Complexity

- **Time:** O(n) -- each phase is at most O(n).
- **Space:** O(1) -- only two pointers.
