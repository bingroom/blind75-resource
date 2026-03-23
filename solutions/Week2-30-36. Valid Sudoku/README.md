# Valid Sudoku

**Topic:** Matrix
- **LeetCode 連結:** [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
- **難度:** Medium

## 題目描述

判斷一個 9x9 的數獨是否有效。只需驗證已填入的數字是否滿足規則：每一行、每一列、每個 3x3 宮格內的數字均不重複。不需要驗證數獨是否有解。

## 解題思路

1. 建立 9 個行集合、9 個列集合和 9 個宮格集合。
2. 遍歷整個 9x9 棋盤的每個格子。
3. 跳過空格（'.'），對已填數字檢查是否已存在於對應的行、列或宮格集合中。
4. 若重複則回傳 false，否則將數字加入對應集合。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(1) — the board is always 9x9 (81 cells).
- **空間複雜度:** O(1) — sets hold at most 9 elements each, constant total.
