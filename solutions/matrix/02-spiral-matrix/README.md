# Spiral Matrix

- **LeetCode:** [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 10`

	- `-100 <= matrix[i][j] <= 100`

## Solution

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

## 思路

- **邊界法：** 維護 top/bottom/left/right，依序輸出上邊、右邊、下邊、左邊，每輪後收縮邊界，注意最後兩邊可能只剩一行/一列需判斷。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(1) 額外（不含輸出）。

## 相關閱讀

- **演算法:** 邊界收縮、模擬
