# Median of Two Sorted Arrays

- **LeetCode:** [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log(min(m, n))).

## Approach

**Binary search** on the partition of the shorter array:

1. Always binary-search on the shorter array to guarantee O(log(min(m, n))).
2. We want to split both arrays into left and right halves such that the combined left half has `(m + n + 1) // 2` elements.
3. Let `i` be the partition point in `nums1` and `j = half - i` in `nums2`.
4. A valid partition satisfies `max(left1, left2) <= min(right1, right2)`.
5. If `left1 > right2`, move the partition left in `nums1`; if `left2 > right1`, move it right.
6. Once valid, the median is `max(left1, left2)` for odd total length, or the average of `max(left1, left2)` and `min(right1, right2)` for even.

## Complexity

- **Time:** O(log(min(m, n))) -- binary search on the shorter array.
- **Space:** O(1) -- constant extra space.
