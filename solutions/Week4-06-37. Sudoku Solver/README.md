# Sudoku Solver

**Topic:** Matrix
- **LeetCode 連結:** [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
- **難度:** Hard

## 題目描述

編寫程式解數獨。填入數字 1-9，使得每行、每列和每個 3x3 宮格中數字不重複。

## 解題思路

1. 初始化三組集合分別追蹤每行、每列和每個 3x3 宮格已使用的數字。
2. 使用回溯法，找到下一個空格。
3. 嘗試填入 1-9，若不與行、列、宮格衝突則填入並遞迴處理下一格。
4. 若所有數字都不可行，回溯清除當前格。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(9^m) where m is the number of empty cells (heavily pruned in practice)
- **空間複雜度:** O(m) for the recursion stack, plus O(81) for the constraint sets
