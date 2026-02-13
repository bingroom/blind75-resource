# LeetCode 200. Number of Islands
# 時間複雜度: O(m * n)  空間複雜度: O(m * n) 遞迴
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        '1' 陸地、'0' 水，求島嶼數。對每個未訪的 '1' DFS/BFS 並標記為已訪，島嶼數即 DFS 次數。
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(r + dr, c + dc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count
