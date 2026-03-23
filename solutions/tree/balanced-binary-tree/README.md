# Balanced Binary Tree

## Problem Description
Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is one in which the depth of the two subtrees of every node never differs by more than one.

## Approach
Use bottom-up recursion that returns the height of each subtree. If at any node the left and right heights differ by more than 1, return -1 to signal imbalance. This avoids redundant height calculations compared to a top-down approach.

1. Base case: null node has height 0.
2. Recursively get left and right subtree heights.
3. If either returns -1, propagate -1 (already unbalanced).
4. If `abs(left - right) > 1`, return -1.
5. Otherwise return `1 + max(left, right)`.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(h) -- recursion stack, where h is tree height.
