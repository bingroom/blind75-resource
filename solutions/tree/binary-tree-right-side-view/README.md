# Binary Tree Right Side View

## Problem Description
Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.

## Approach
Use BFS (level-order traversal). For each level, the last node in the queue is the rightmost node visible from the right side.

1. Initialize a queue with the root.
2. For each level, iterate through all nodes at that level.
3. The last node processed in each level is the right-side-visible node.
4. Add children (left then right) to the queue.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(n) -- queue can hold up to n/2 nodes at the widest level.
