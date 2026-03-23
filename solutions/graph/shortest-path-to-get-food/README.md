# Shortest Path to Get Food

- **LeetCode:** [1730. Shortest Path to Get Food](https://leetcode.com/problems/shortest-path-to-get-food/)

## Problem Description

Given an `m x n` grid where `'*'` is your starting position, `'#'` is food, `'O'` is free space, and `'X'` is an obstacle, return the length of the shortest path to reach any food cell. Return `-1` if no food is reachable.

## Approach

Standard BFS from the starting position:

1. Locate the `'*'` cell and enqueue it with distance 0.
2. BFS outward, skipping obstacles (`'X'`) and visited cells.
3. Return immediately when a food cell (`'#'`) is reached.
4. If the queue empties without finding food, return -1.

## Complexity

- **Time:** O(m * n) -- each cell visited at most once.
- **Space:** O(m * n) -- queue and visited markers.
