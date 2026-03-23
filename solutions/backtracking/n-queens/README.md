# N-Queens

- **LeetCode:** [51. N-Queens](https://leetcode.com/problems/n-queens/)

## Problem Description

Place `n` queens on an `n x n` chessboard such that no two queens attack each other. Return all distinct solutions, where each solution is a board configuration with `'Q'` and `'.'`.

## Approach

Backtracking row by row with three sets to track attacked columns and diagonals.

1. Place one queen per row. For each row, try every column.
2. A column is safe if it is not in `cols`, and neither diagonal `(row - col)` nor anti-diagonal `(row + col)` is occupied.
3. Place the queen, update the three sets, and recurse to the next row.
4. When `row == n`, all queens are placed -- record the board.
5. Backtrack: remove the queen and restore the sets.

Using `row - col` for one diagonal direction and `row + col` for the other uniquely identifies each diagonal line.

## Complexity

- **Time:** O(n!) -- at most n choices in row 0, n-1 in row 1, etc.
- **Space:** O(n) for the sets and recursion stack
