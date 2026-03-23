# Generate Parentheses

**Topic:** Recursion
- **LeetCode 連結:** [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- **難度:** Medium

## 題目描述

給定 n 對括號，生成所有合法的括號組合。

## 解題思路

1. 使用回溯法，追蹤已使用的左括號與右括號數量。
2. 若左括號數量小於 n，可以放入左括號。
3. 若右括號數量小於左括號數量，可以放入右括號。
4. 當路徑長度等於 2n 時，將結果加入答案。

## 程式碼

```python
# LeetCode 22. Generate Parentheses
# Time: O(4^n / sqrt(n)) (nth Catalan number)  Space: O(n)

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path: List[str], open_count: int, close_count: int):
            if len(path) == 2 * n:
                result.append(''.join(path))
                return
            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return result
```

## 複雜度分析

- **時間複雜度:** O(4^n / sqrt(n)) -- the nth Catalan number bounds the number of valid combinations
- **空間複雜度:** O(n) for the recursion depth
