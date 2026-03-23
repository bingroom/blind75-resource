# Graph Valid Tree

- **LeetCode:** [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

## Problem Description

Given `n` nodes labeled `0` to `n - 1` and a list of undirected edges, determine if these edges form a valid tree. A valid tree is a connected acyclic graph.

## Approach

Union-Find:

1. A tree with `n` nodes must have exactly `n - 1` edges. If not, return False immediately.
2. Process each edge with Union-Find. If both endpoints already share the same root, a cycle exists -- return False.
3. If all edges are processed without a cycle and the edge count is `n - 1`, the graph is a valid tree.

## Complexity

- **Time:** O(n * alpha(n)) where alpha is the inverse Ackermann function.
- **Space:** O(n) -- parent and rank arrays.
