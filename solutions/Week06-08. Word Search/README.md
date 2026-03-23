# Word Search

**Topic:** Backtracking

- **LeetCode:** [79. Word Search](https://leetcode.com/problems/word-search/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

```

 

**Constraints:**

	- `m == board.length`

	- `n = board[i].length`

	- `1 <= m, n <= 6`

	- `1 <= word.length <= 15`

	- `board` and `word` consists of only lowercase and uppercase English letters.

 

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

## Solution

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

## 思路

- **DFS + 回溯：** 從每個格子出發嘗試匹配 word，用過格暫時標記（如改為 '#'），遞迴後還原，以便其他路徑使用。

## 時間 / 空間複雜度

- **時間:** O(m×n×4^L)，L 為 word 長度。
- **空間:** O(L) 遞迴棧。

## 相關閱讀

- **演算法:** DFS、Backtracking
