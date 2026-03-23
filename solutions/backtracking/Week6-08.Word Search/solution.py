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
