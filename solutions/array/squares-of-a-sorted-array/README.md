# Squares of a Sorted Array

- **LeetCode:** [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Approach

Use a **two-pointer** technique:

1. Place pointers at the leftmost and rightmost elements.
2. The largest squared value must come from one of these two ends (large negatives or large positives).
3. Compare `abs(nums[left])` and `abs(nums[right])`. Place the larger square at the back of the result array.
4. Move the chosen pointer inward and repeat, filling the result from right to left.

## Complexity

- **Time:** O(n) -- single pass with two pointers.
- **Space:** O(n) -- for the output array.
