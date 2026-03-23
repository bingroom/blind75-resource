# Combination Sum

**Topic:** Array
- **LeetCode 連結:** [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- **難度:** Medium

## 題目描述

給定一個無重複元素的整數陣列 candidates 和一個目標值 target，找出所有和為 target 的組合。每個數字可以被無限次重複選取，組合不可重複。

## 解題思路

1. 使用回溯法，維護目前的路徑和剩餘目標值。
2. 從 start 索引開始遍歷候選數，若候選數大於剩餘值則跳過。
3. 將候選數加入路徑，遞迴時傳入相同索引（允許重複使用）。
4. 當剩餘值為 0 時，將當前路徑加入結果。
5. 遞迴返回後移除最後加入的數字（回溯）。

## 程式碼

```python
# LeetCode 39. Combination Sum
# Time: O(n^(target/min))  Space: O(target/min) recursion depth

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    continue
                path.append(c)
                # Pass i (not i+1) because we can reuse the same element
                backtrack(i, remaining - c, path)
                path.pop()

        backtrack(0, target, [])
        return result
```

## 複雜度分析

- **時間複雜度:** O(n^(target/min)) in the worst case, where min is the smallest candidate
- **空間複雜度:** O(target/min) for the recursion depth
