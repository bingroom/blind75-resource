# Maximum Width of Binary Tree

## Problem Description
Given the root of a binary tree, return the maximum width of the tree. The width of one level is defined as the length between the leftmost and rightmost non-null nodes (including null nodes in between).

## Approach
BFS with index tracking. Assign each node a position index (root = 0). For a node at index `i`, its left child is at `2*i` and right child at `2*i + 1`.

1. Use a queue storing `(node, index)` pairs.
2. At each level, normalize indices by subtracting the first index (prevents integer overflow in deep/skewed trees).
3. Width of a level = last index - first index + 1.
4. Track the global maximum width.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(n) -- queue can hold up to n/2 nodes.
