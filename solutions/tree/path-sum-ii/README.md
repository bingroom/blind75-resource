# Path Sum II

## Problem Description
Given the root of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of node values equals `targetSum`.

## Approach
DFS with backtracking:

1. Maintain a running path list and remaining sum.
2. At each node, append its value and subtract from remaining.
3. At a leaf, if remaining equals 0, copy the current path to results.
4. After exploring children, pop the current node (backtrack).

## Complexity
- **Time:** O(n) -- visit every node; copying paths costs O(h) each but bounded by O(n * h) total.
- **Space:** O(h) -- recursion stack and current path.
