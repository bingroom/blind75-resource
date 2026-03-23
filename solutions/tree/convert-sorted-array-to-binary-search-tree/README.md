# Convert Sorted Array to Binary Search Tree

## Problem Description
Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

## Approach
Recursively pick the middle element of the current range as the root. This guarantees height balance since the left and right halves differ by at most one element.

1. Base case: if `lo > hi`, return null.
2. Pick `mid = (lo + hi) // 2` as root.
3. Recursively build left subtree from `[lo, mid-1]`.
4. Recursively build right subtree from `[mid+1, hi]`.

## Complexity
- **Time:** O(n) -- each element visited once.
- **Space:** O(log n) -- recursion stack for a balanced tree.
