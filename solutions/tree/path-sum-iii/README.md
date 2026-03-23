# Path Sum III

## Problem Description
Given the root of a binary tree and an integer `targetSum`, return the number of paths where the sum of values along the path equals `targetSum`. The path does not need to start at the root or end at a leaf, but must go downwards (from parent to child).

## Approach
Prefix sum technique (similar to subarray sum equals k):

1. Maintain a hash map of prefix sum frequencies along the current root-to-node path.
2. At each node, compute `curr_sum` (cumulative sum from root).
3. Check how many times `curr_sum - targetSum` appeared as a prefix sum -- each occurrence represents a valid path ending at this node.
4. Add `curr_sum` to the map, recurse into children, then backtrack by decrementing the count.

This reduces the problem from O(n^2) brute force to O(n).

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(n) -- prefix sum map and recursion stack.
