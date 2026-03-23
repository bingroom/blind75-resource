# Subsets

**Topic:** Recursion
- **LeetCode 連結:** [78. Subsets](https://leetcode.com/problems/subsets/)
- **難度:** Medium

## 題目描述

給定一個不含重複元素的整數陣列，回傳其所有可能的子集（冪集）。結果不可包含重複的子集，可以按任意順序回傳。

## 解題思路

1. 使用回溯法，每個遞迴狀態下的路徑都是一個合法的子集，加入結果。
2. 從 start 索引開始遍歷，將當前元素加入路徑。
3. 遞迴時傳入 i + 1 以避免重複選取同一元素。
4. 遞迴返回後移除最後的元素（回溯），嘗試下一個元素。

## 程式碼

```python
# LeetCode 78. Subsets
# Time: O(n * 2^n)  Space: O(n) recursion depth

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path[:])  # Every path is a valid subset
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
```

## 複雜度分析

- **時間複雜度:** O(n * 2^n) -- 2^n subsets, each takes O(n) to copy
- **空間複雜度:** O(n) for the recursion depth
