# LeetCode 733. Flood Fill
# Time: O(m * n)  Space: O(m * n)

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return
            image[r][c] = color
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image
