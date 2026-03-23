# Minimum Knight Moves

- **LeetCode:** [1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/)

## Problem Description

In an infinite chess board with coordinates from `-infinity` to `+infinity`, a knight starts at `(0, 0)`. Return the minimum number of moves to reach `(x, y)`.

## Approach

BFS exploiting symmetry:

1. Map the target to the first quadrant using `abs(x)`, `abs(y)` since the board is symmetric.
2. BFS from `(0, 0)` exploring all 8 knight moves.
3. Restrict exploration to coordinates >= -1 (a small negative margin is needed to handle edge cases near the origin like `(1, 0)`).
4. Return the step count when we reach the target.

## Complexity

- **Time:** O(|x| * |y|) -- the BFS explores a bounded region around the target.
- **Space:** O(|x| * |y|) -- visited set.
