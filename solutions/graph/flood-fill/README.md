# Flood Fill

- **LeetCode:** [733. Flood Fill](https://leetcode.com/problems/flood-fill/)

## Problem Description

Given an `m x n` integer grid `image`, a starting pixel `(sr, sc)`, and an integer `color`, perform a flood fill starting from the pixel `image[sr][sc]`. Change the color of the starting pixel and all adjacent (4-directionally) pixels of the same original color to `color`. Return the modified image.

## Approach

1. Record the original color at `(sr, sc)`. If it already equals `color`, return immediately to avoid infinite loops.
2. Run DFS from `(sr, sc)`: change the current pixel to `color`, then recurse on all four neighbors that still have the original color.

## Complexity

- **Time:** O(m * n) -- each pixel visited at most once.
- **Space:** O(m * n) -- recursion stack in the worst case.
