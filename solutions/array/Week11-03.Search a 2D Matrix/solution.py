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
