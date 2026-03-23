# Search a 2D Matrix

**Topic:** Binary Search
- **LeetCode 連結:** [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- **難度:** Medium

## 題目描述

給定一個 m x n 矩陣，每行從左到右遞增，且每行第一個元素大於上一行最後一個元素。判斷目標值是否存在於矩陣中。

## 解題思路

1. 將二維矩陣視為一維排序陣列，進行標準二分搜尋。
2. 用 divmod 將一維索引轉換為二維的行列座標。
3. 比較中間元素與目標值，縮小搜尋範圍直到找到或確認不存在。

## 程式碼

```python
# LeetCode 74. Search a 2D Matrix
# Time: O(log(m * n))  Space: O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Treat the 2D matrix as a flattened sorted array and run standard
        binary search. Map the 1D index to (row, col) with divmod.
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

## 複雜度分析

- **時間複雜度:** O(log(m * n)) -- single binary search.
- **空間複雜度:** O(1) -- no extra data structures.
