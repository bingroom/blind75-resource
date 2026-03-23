# N-Queens

**Topic:** Recursion
- **LeetCode 連結:** [51. N-Queens](https://leetcode.com/problems/n-queens/)
- **難度:** Hard

## 題目描述

N 皇后問題：在 n x n 棋盤上放置 n 個皇后，使其彼此不能互相攻擊。回傳所有不同的解法。

## 解題思路

1. 使用回溯法逐行放置皇后。
2. 用三個集合分別記錄已佔用的列、主對角線和副對角線。
3. 對每一行嘗試每一列，若不與已放置的皇后衝突則放置。
4. 遞迴處理下一行，完成所有行後記錄解法。回溯時移除皇后。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n!) -- at most n choices in row 0, n-1 in row 1, etc.
- **空間複雜度:** O(n) for the sets and recursion stack
