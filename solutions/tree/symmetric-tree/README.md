# Symmetric Tree

## Problem Description
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Approach
Use a recursive helper that checks if two subtrees are mirror images:

1. If both nodes are null, they are mirrors.
2. If only one is null, not mirrors.
3. Otherwise, values must match, and `left.left` must mirror `right.right`, and `left.right` must mirror `right.left`.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(h) -- recursion stack.
