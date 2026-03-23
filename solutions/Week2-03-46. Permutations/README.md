# Permutations

**Topic:** Recursion
- **LeetCode 連結:** [46. Permutations](https://leetcode.com/problems/permutations/)
- **難度:** Medium

## 題目描述

給定一個不含重複數字的整數陣列，回傳其所有可能的排列。可以按任意順序回傳結果。

## 解題思路

1. 使用回溯法，維護當前路徑 path 和已使用的數字集合 used。
2. 當 path 長度等於陣列長度時，將路徑的副本加入結果。
3. 遍歷所有數字，若尚未使用則加入路徑和 used 集合，遞迴繼續。
4. 遞迴返回後移除最後的數字並從 used 中刪除（回溯）。

## 程式碼

```python
# LeetCode 46. Permutations
# Time: O(n * n!)  Space: O(n)

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path: List[int], used: set):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num in used:
                    continue
                used.add(num)
                path.append(num)
                backtrack(path, used)
                path.pop()
                used.remove(num)

        backtrack([], set())
        return result
```

## 複雜度分析

- **時間複雜度:** O(n * n!) -- n! permutations, each takes O(n) to copy
- **空間複雜度:** O(n) for the recursion stack and used set
