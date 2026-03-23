# Word Search

**Topic:** Graph
- **LeetCode 連結:** [79. Word Search](https://leetcode.com/problems/word-search/)
- **難度:** Medium

## 題目描述

給定一個二維字元網格和一個單字，判斷該單字是否存在於網格中。單字必須由相鄰格子（上下左右）的字母依序構成，且同一格子不能重複使用。

## 解題思路

1. 遍歷網格中每個格子作為起點，嘗試匹配單字的第一個字母。
2. 使用 DFS 向上下左右四個方向搜尋下一個字母。
3. 將已使用的格子標記（如改為 '#'）以避免重複訪問。
4. 若成功匹配完整個單字，回傳 true。
5. 回溯時將格子還原為原始字母。

## 程式碼

```python
# LeetCode 79. Word Search
# 時間複雜度: O(m * n * 4^len(word))  空間複雜度: O(len(word))
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        在二維網格中找相鄰（上下左右）是否可組成 word。DFS + 回溯，用過格標記後還原。
        """
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
                return False
            board[r][c], orig = "#", board[r][c]
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if dfs(r + dr, c + dc, i + 1):
                    return True
            board[r][c] = orig
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
```

## 複雜度分析

- **時間複雜度:** O(m×n×4^L)，L 為 word 長度。
- **空間複雜度:** O(L) 遞迴棧。
