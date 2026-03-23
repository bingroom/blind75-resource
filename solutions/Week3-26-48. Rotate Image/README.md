# Rotate Image

**Topic:** Matrix
- **LeetCode 連結:** [48. Rotate Image](https://leetcode.com/problems/rotate-image/)
- **難度:** Medium

## 題目描述

給定一個 n x n 的二維矩陣，將其順時針旋轉 90 度。需原地操作，不使用額外矩陣。

## 解題思路

1. 先沿主對角線轉置矩陣（交換 matrix[i][j] 與 matrix[j][i]）。
2. 再將每一行左右翻轉。
3. 兩步操作等價於順時針旋轉 90 度。

## 程式碼

```python
# LeetCode 48. Rotate Image
# 時間複雜度: O(n²)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        將 n×n 矩陣順時針旋轉 90 度，in-place。先沿主對角線反轉，再左右翻轉；或一圈一圈換四個角。
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for r in range(n):
            matrix[r].reverse()
```

## 複雜度分析

- **時間複雜度:** O(n²)。
- **空間複雜度:** O(1)。
