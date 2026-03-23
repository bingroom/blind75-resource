# All Nodes Distance K in Binary Tree

## Problem Description
Given the root of a binary tree, a target node, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

## Approach
Convert the tree into an undirected graph, then BFS from the target:

1. **Build parent map:** DFS through the tree to record each node's parent, enabling upward traversal.
2. **BFS from target:** Treat the tree as an undirected graph (each node connects to left child, right child, and parent). BFS outward from target, tracking visited nodes.
3. When BFS reaches distance `k`, return all nodes in the current queue.

## Complexity
- **Time:** O(n) -- DFS to build parent map + BFS visits each node at most once.
- **Space:** O(n) -- parent map, visited set, and BFS queue.
