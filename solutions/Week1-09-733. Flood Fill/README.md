# Flood Fill

**Topic:** Graph
- **LeetCode 連結:** [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
- **難度:** Easy

## 題目描述

給定一個二維整數陣列代表圖片、一個起始座標 `(sr, sc)` 和一個新顏色 `color`，從起始像素開始執行填色操作：將所有與起始像素相連且顏色相同的像素都改為新顏色。

## 解題思路

1. 記錄起始像素的原始顏色；若原始顏色與新顏色相同，直接回傳（避免無限遞迴）。
2. 從起始座標開始執行 DFS。
3. 將當前像素改為新顏色，然後遞迴處理上下左右四個相鄰像素。
4. 遞迴時檢查邊界條件及像素顏色是否為原始顏色。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(m * n) -- each pixel visited at most once.
- **空間複雜度:** O(m * n) -- recursion stack in the worst case.
