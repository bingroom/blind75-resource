# Two Sum

**Topic:** Array
- **LeetCode 連結:** [1. Two Sum](https://leetcode.com/problems/two-sum/)
- **難度:** Easy

## 題目描述

給定一個整數陣列 `nums` 和一個目標值 `target`，找出陣列中兩個數字的索引，使它們的和等於目標值。每個輸入恰好有一個解，且不能重複使用同一元素。

## 解題思路

1. 使用雜湊表儲存已遍歷的數字及其索引。
2. 遍歷陣列，對每個數字計算其補數（target - num）。
3. 若補數已存在於雜湊表中，回傳兩個索引。
4. 否則將當前數字加入雜湊表，繼續遍歷。

## 程式碼

```python
# LeetCode 1. Two Sum
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        在陣列中找兩數之和等於 target，回傳兩數的索引。
        使用 Hash Map 一次遍歷：邊走邊查「target - 當前值」是否已出現。
        """
        # seen[數值] = 索引，用來 O(1) 查詢「互補數」是否出現過
        seen = {}
        for i, x in enumerate(nums):
            # 互補數 = target - 當前數，若在 seen 裡表示之前已出現過
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
```

## 複雜度分析

- **時間複雜度:** O(n)，單次遍歷 + 查表 O(1)。
- **空間複雜度:** O(n)，最壞存 n 個數。
