# Valid Sudoku

- **LeetCode:** [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

## Problem Description

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to three rules: each row, each column, and each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.


## Solution

```python
# LeetCode 36. Valid Sudoku
# Time: O(81) = O(1)  Space: O(81) = O(1)


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Validate a 9x9 Sudoku board. Only filled cells need to be checked:
        no duplicate in any row, column, or 3x3 sub-box.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box_idx = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True
```

## Approach

1. Maintain three groups of hash sets: one per row, one per column, and one per 3x3 box (9 sets each).
2. Iterate over every cell. Skip `'.'` (empty).
3. Compute the box index as `(row // 3) * 3 + (col // 3)`.
4. If the digit already exists in the corresponding row, column, or box set, the board is invalid.
5. Otherwise add the digit to all three sets and continue.

## Complexity

- **Time:** O(1) — the board is always 9x9 (81 cells).
- **Space:** O(1) — sets hold at most 9 elements each, constant total.
