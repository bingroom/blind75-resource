# Spiral Matrix

**Topic:** Matrix
- **LeetCode 連結:** [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- **難度:** Medium

## 題目描述

給定一個 m x n 的矩陣，以螺旋順序（順時針由外向內）回傳矩陣中的所有元素。

## 解題思路

1. 維護上、下、左、右四個邊界。
2. 依序遍歷：上邊從左到右、右邊從上到下、下邊從右到左、左邊從下到上。
3. 每完成一個方向後收縮對應的邊界。
4. 注意在遍歷下邊和左邊前，需檢查邊界是否仍合法，避免重複遍歷。
5. 重複直到所有邊界交錯為止。

## 程式碼

```python
# LeetCode 54. Spiral Matrix
# 時間複雜度: O(m * n)  空間複雜度: O(1) 不含輸出
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        依螺旋順序回傳矩陣元素。維護上下左右邊界，依序：上邊從左到右、右邊從上到下、下邊從右到左、左邊從下到上，每次收縮邊界。
        """
        if not matrix or not matrix[0]:
            return []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        out = []
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                out.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                out.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    out.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    out.append(matrix[r][left])
                left += 1
        return out
```

## 複雜度分析

- **時間複雜度:** O(m×n)。
- **空間複雜度:** O(1) 額外（不含輸出）。
