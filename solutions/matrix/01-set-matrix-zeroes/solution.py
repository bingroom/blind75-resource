# LeetCode 73. Set Matrix Zeroes
# 時間複雜度: O(m * n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        若某格為 0，將該行該列全設為 0，要求 O(1) 空間。用第一行、第一列當標記，先記下第一行/列是否要變 0。
        """
        m, n = len(matrix), len(matrix[0])
        row0 = any(matrix[0][c] == 0 for c in range(n))
        col0 = any(matrix[r][0] == 0 for r in range(m))
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if row0:
            for c in range(n):
                matrix[0][c] = 0
        if col0:
            for r in range(m):
                matrix[r][0] = 0
