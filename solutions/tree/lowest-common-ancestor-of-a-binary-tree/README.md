# Lowest Common Ancestor of a Binary Tree

## Problem Description
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q. The LCA is the lowest node that has both p and q as descendants (a node can be a descendant of itself).

## Approach
Recursive post-order traversal:

1. If the current node is null, p, or q, return it.
2. Recurse into left and right subtrees.
3. If both sides return non-null, the current node is the LCA (p and q are in different subtrees).
4. If only one side returns non-null, propagate that result upward.

## Complexity
- **Time:** O(n) -- worst case visits all nodes.
- **Space:** O(h) -- recursion stack.
