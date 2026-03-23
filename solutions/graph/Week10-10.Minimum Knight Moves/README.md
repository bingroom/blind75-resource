# Minimum Knight Moves

- **LeetCode:** [1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/)

## Problem Description

In an infinite chess board with coordinates from `-infinity` to `+infinity`, a knight starts at `(0, 0)`. Return the minimum number of moves to reach `(x, y)`.


## Solution

```python
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
```

## Approach

BFS exploiting symmetry:

1. Map the target to the first quadrant using `abs(x)`, `abs(y)` since the board is symmetric.
2. BFS from `(0, 0)` exploring all 8 knight moves.
3. Restrict exploration to coordinates >= -1 (a small negative margin is needed to handle edge cases near the origin like `(1, 0)`).
4. Return the step count when we reach the target.

## Complexity

- **Time:** O(|x| * |y|) -- the BFS explores a bounded region around the target.
- **Space:** O(|x| * |y|) -- visited set.
