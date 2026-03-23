# Rotate List

- **LeetCode:** [61. Rotate List](https://leetcode.com/problems/rotate-list/)

## Problem Description
Given the `head` of a linked list, rotate the list to the right by `k` places.

## Approach
1. **Count the length** of the list and find the tail node in one pass.
2. **Reduce k:** Compute `k % length` since rotating by the full length is a no-op.
3. **Find the new tail:** Walk `length - k - 1` steps from the head. The node after this becomes the new head.
4. **Relink:** Break the list at the new tail, and connect the old tail to the old head.

This effectively moves the last `k` nodes to the front without any extra space.

## Complexity
- **Time:** O(n) -- two passes at most (one to count, one to find the split point).
- **Space:** O(1) -- only pointer variables.
