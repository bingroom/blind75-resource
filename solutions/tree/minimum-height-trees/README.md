# Minimum Height Trees

## Problem Description
Given a tree of `n` nodes labeled `0` to `n-1` and `n-1` edges, find all roots that minimize the tree's height (Minimum Height Trees). Return a list of their labels.

## Approach
Topological leaf trimming (like peeling an onion):

1. Build an adjacency list. Identify all leaf nodes (degree 1).
2. Repeatedly remove all current leaves and update neighbor degrees.
3. Nodes that become degree 1 after removal are the new leaves.
4. Continue until 1 or 2 nodes remain -- these are the MHT roots.

The intuition: the center of the longest path in a tree minimizes the maximum distance to any node. Trimming from the outside converges to this center.

## Complexity
- **Time:** O(n) -- each node and edge processed once.
- **Space:** O(n) -- adjacency list and queue.
