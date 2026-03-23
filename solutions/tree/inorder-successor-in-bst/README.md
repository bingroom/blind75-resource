# Inorder Successor in BST

## Problem Description
Given the root of a BST and a node `p`, find the in-order successor of `p` (the node with the smallest key greater than `p.val`). Return null if no successor exists.

## Approach
Leverage BST ordering -- no need for full inorder traversal:

1. If current node's value is greater than p's value, it is a potential successor. Record it and go left to find a smaller candidate.
2. If current node's value is less than or equal to p's value, the successor must be in the right subtree. Go right.
3. When traversal ends, the last recorded candidate is the answer.

## Complexity
- **Time:** O(h) -- single root-to-leaf traversal.
- **Space:** O(1) -- iterative, no extra space.
