# LeetCode 1197. Minimum Knight Moves
# Time: O(|x| * |y|)  Space: O(|x| * |y|)
# BFS in first quadrant using symmetry

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # By symmetry we only need to consider the first quadrant
        x, y = abs(x), abs(y)

        q = deque([(0, 0, 0)])  # (row, col, steps)
        visited = {(0, 0)}
        moves = [(1, 2), (2, 1), (2, -1), (1, -2),
                 (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        while q:
            cx, cy, steps = q.popleft()
            if cx == x and cy == y:
                return steps
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                # Allow small negative coords (-1) to handle edge cases near origin
                if (nx, ny) not in visited and nx >= -1 and ny >= -1:
                    visited.add((nx, ny))
                    q.append((nx, ny, steps + 1))

        return -1
