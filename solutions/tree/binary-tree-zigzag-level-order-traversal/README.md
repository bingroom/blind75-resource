# Binary Tree Zigzag Level Order Traversal

## Problem Description
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values (i.e., from left to right, then right to left for the next level, and alternate between).

## Approach
Standard BFS level-order traversal with a direction flag:

1. Process each level left-to-right using a queue.
2. Maintain a boolean flag that alternates each level.
3. On even levels (0-indexed), keep order as-is; on odd levels, reverse the level list.

## Complexity
- **Time:** O(n) -- each node visited once; reversing a level is O(level size).
- **Space:** O(n) -- queue and result storage.
