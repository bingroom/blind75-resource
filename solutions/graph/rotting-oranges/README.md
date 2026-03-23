# Rotting Oranges

- **LeetCode:** [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

## Problem Description

In a grid, `0` represents an empty cell, `1` a fresh orange, and `2` a rotten orange. Every minute, any fresh orange adjacent (4-directionally) to a rotten orange becomes rotten. Return the minimum number of minutes until no fresh orange remains, or `-1` if impossible.

## Approach

Multi-source BFS:

1. Enqueue all initially rotten oranges and count fresh oranges.
2. BFS level by level; each level represents one minute. For each rotten orange, rot its fresh neighbors and decrement the fresh count.
3. If fresh reaches 0, return the current minute count. If BFS ends with fresh > 0, return -1.

## Complexity

- **Time:** O(m * n) -- each cell processed at most once.
- **Space:** O(m * n) -- queue size in the worst case.
