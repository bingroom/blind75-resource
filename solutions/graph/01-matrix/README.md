# 01 Matrix

- **LeetCode:** [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)

## Problem Description

Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell. The distance between two adjacent cells is `1`.

## Approach

Multi-source BFS starting from all `0` cells at once:

1. Initialize a distance matrix. Set distance to `0` for all `0`-cells and `inf` for all `1`-cells.
2. Enqueue all `0`-cells.
3. BFS outward: for each dequeued cell, check all four neighbors. If the neighbor's recorded distance is greater than current + 1, update it and enqueue.

This guarantees each cell is visited with its shortest distance first.

## Complexity

- **Time:** O(m * n) -- each cell enqueued at most once.
- **Space:** O(m * n) -- distance matrix and queue.
