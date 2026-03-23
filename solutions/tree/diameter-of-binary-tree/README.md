# Diameter of Binary Tree

## Problem Description
Given the root of a binary tree, return the length of the diameter of the tree. The diameter is the length of the longest path between any two nodes (measured in number of edges). This path may or may not pass through the root.

## Approach
Compute the height of each subtree bottom-up. At each node, the longest path passing through it equals `left_height + right_height`. Track the global maximum across all nodes.

1. Base case: null node has height 0.
2. Recursively compute left and right heights.
3. Update global max with `left + right`.
4. Return `1 + max(left, right)` as this node's height.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(h) -- recursion stack.
