# Search a 2D Matrix

- **LeetCode:** [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

## Problem Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix. The matrix has the following properties: integers in each row are sorted left to right, and the first integer of each row is greater than the last integer of the previous row.

## Approach

**Binary search** on the virtual flattened array:

1. The matrix is fully sorted when read row by row, so treat it as a 1D sorted array of length `m * n`.
2. Perform standard binary search with `left = 0` and `right = m * n - 1`.
3. Convert the 1D midpoint to 2D coordinates using `row, col = divmod(mid, n)`.
4. Compare `matrix[row][col]` with `target` and adjust bounds accordingly.

## Complexity

- **Time:** O(log(m * n)) -- single binary search.
- **Space:** O(1) -- no extra data structures.
