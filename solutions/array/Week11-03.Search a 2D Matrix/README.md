# Search a 2D Matrix

- **LeetCode:** [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

## Problem Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix. The matrix has the following properties: integers in each row are sorted left to right, and the first integer of each row is greater than the last integer of the previous row.


## Solution

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

## Approach

**Binary search** on the virtual flattened array:

1. The matrix is fully sorted when read row by row, so treat it as a 1D sorted array of length `m * n`.
2. Perform standard binary search with `left = 0` and `right = m * n - 1`.
3. Convert the 1D midpoint to 2D coordinates using `row, col = divmod(mid, n)`.
4. Compare `matrix[row][col]` with `target` and adjust bounds accordingly.

## Complexity

- **Time:** O(log(m * n)) -- single binary search.
- **Space:** O(1) -- no extra data structures.
