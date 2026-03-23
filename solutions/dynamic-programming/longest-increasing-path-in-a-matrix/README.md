# Longest Increasing Path in a Matrix

- **LeetCode:** [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## Problem Description

Given an `m x n` integers matrix, return the length of the longest increasing path in the matrix. From each cell, you can move in four directions (up, down, left, right). You may not move diagonally or outside the boundary.

## Approach

DFS with memoization. Since the path must be strictly increasing, there are no cycles, making memoization safe without a visited set.

1. For each cell `(i, j)`, run DFS to find the longest increasing path starting from that cell.
2. At each cell, try all four directions. If the neighbor has a strictly larger value, recurse and take the max path length + 1.
3. Cache the result for each cell to avoid recomputation. Each cell is computed exactly once.
4. Return the maximum over all cells.

## Complexity

- **Time:** O(m * n) -- each cell is visited and computed exactly once due to memoization
- **Space:** O(m * n) -- for the memo table and recursion stack
