# Flood Fill

- **LeetCode:** [733. Flood Fill](https://leetcode.com/problems/flood-fill/)

## Problem Description

Given an `m x n` integer grid `image`, a starting pixel `(sr, sc)`, and an integer `color`, perform a flood fill starting from the pixel `image[sr][sc]`. Change the color of the starting pixel and all adjacent (4-directionally) pixels of the same original color to `color`. Return the modified image.


## Solution

```python
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
```

## Approach

1. Record the original color at `(sr, sc)`. If it already equals `color`, return immediately to avoid infinite loops.
2. Run DFS from `(sr, sc)`: change the current pixel to `color`, then recurse on all four neighbors that still have the original color.

## Complexity

- **Time:** O(m * n) -- each pixel visited at most once.
- **Space:** O(m * n) -- recursion stack in the worst case.
