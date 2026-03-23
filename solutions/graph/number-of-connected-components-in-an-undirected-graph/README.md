# Number of Connected Components in an Undirected Graph

- **LeetCode:** [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

## Problem Description

Given `n` nodes labeled `0` to `n - 1` and a list of undirected edges, return the number of connected components in the graph.

## Approach

Union-Find with path compression and union by rank:

1. Initialize each node as its own component (count = n).
2. For each edge, union the two endpoints. If they were in different components, decrement the component count.
3. Return the final count.

## Complexity

- **Time:** O(n + E * alpha(n)) where E is the number of edges and alpha is the inverse Ackermann function.
- **Space:** O(n) -- parent and rank arrays.
