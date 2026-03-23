# Sudoku Solver

- **LeetCode:** [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## Problem Description

Write a program to solve a Sudoku puzzle by filling the empty cells. Each empty cell should be filled with a digit `1-9` such that each row, column, and 3x3 sub-box contains each digit exactly once.

## Approach

Backtracking with constraint propagation using sets for rows, columns, and boxes.

1. Pre-populate sets for each row, column, and 3x3 box with the initial board values.
2. Scan cells left to right, top to bottom. For each empty cell, try digits '1' through '9'.
3. A digit is valid if it is not in the corresponding row set, column set, or box set.
4. Place the digit, update all three sets, and recurse to the next cell.
5. If no digit works, backtrack: remove the digit and restore the sets.
6. When all 81 cells are processed, the board is solved.

## Complexity

- **Time:** O(9^m) where m is the number of empty cells (heavily pruned in practice)
- **Space:** O(m) for the recursion stack, plus O(81) for the constraint sets
