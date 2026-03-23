# Next Permutation

- **LeetCode:** [31. Next Permutation](https://leetcode.com/problems/next-permutation/)

## Problem Description

Given an array of integers `nums`, find the next lexicographically greater permutation of the numbers. If no such permutation exists (the array is sorted in descending order), rearrange it to the lowest possible order (ascending).

The replacement must be in-place and use only constant extra memory.

## Approach

1. **Find the pivot:** Scan from right to left to find the first index `i` where `nums[i] < nums[i + 1]`. The suffix after `i` is non-increasing.
2. **Find the successor:** Scan from the right to find the smallest element larger than `nums[i]`, then swap them.
3. **Reverse the suffix:** Reverse the elements after index `i` to turn the descending suffix into ascending -- producing the smallest next permutation.

If no pivot is found, the entire array is descending, so reversing it gives the first permutation.

## Complexity

- **Time:** O(n) -- at most two linear scans plus one reverse.
- **Space:** O(1) -- all operations are in-place.
