# Sudoku Solver

**Topic:** Backtracking

- **LeetCode:** [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## Problem Description

Write a program to solve a Sudoku puzzle by filling the empty cells. Each empty cell should be filled with a digit `1-9` such that each row, column, and 3x3 sub-box contains each digit exactly once.


## Solution

```python
# LeetCode 37. Sudoku Solver
# Time: O(9^(empty cells))  Space: O(81) for tracking sets

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """Modify board in-place to solve the sudoku."""
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize constraint sets from the given board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(pos: int) -> bool:
            # Find next empty cell starting from pos
            while pos < 81:
                r, c = divmod(pos, 9)
                if board[r][c] == '.':
                    break
                pos += 1
            else:
                return True  # All cells filled

            r, c = divmod(pos, 9)
            box_id = (r // 3) * 3 + c // 3

            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

                    if backtrack(pos + 1):
                        return True

                    # Undo
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)

            return False

        backtrack(0)
```

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
