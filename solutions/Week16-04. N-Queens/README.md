# N-Queens

**Topic:** Backtracking

- **LeetCode:** [51. N-Queens](https://leetcode.com/problems/n-queens/)

## Problem Description

Place `n` queens on an `n x n` chessboard such that no two queens attack each other. Return all distinct solutions, where each solution is a board configuration with `'Q'` and `'.'`.


## Solution

```python
# LeetCode 51. N-Queens
# Time: O(n!)  Space: O(n)

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        board = [['.'] * n for _ in range(n)]

        def backtrack(row: int):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # Remove queen
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result
```

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
