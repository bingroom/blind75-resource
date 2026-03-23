# Merge Intervals

**Topic:** Array
- **LeetCode 連結:** [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- **難度:** Medium

## 題目描述

給定一組區間的集合，將所有重疊的區間合併，並回傳不重疊的區間陣列。

## 解題思路

1. 將區間按起點排序。
2. 初始化結果陣列，放入第一個區間。
3. 遍歷剩餘區間，若當前區間的起點小於等於結果最後一個區間的終點，則合併（取較大的終點）。
4. 否則將當前區間直接加入結果。

## 程式碼

```python
# LeetCode 56. Merge Intervals
# 時間複雜度: O(n log n)  空間複雜度: O(1) 不含輸出
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合併所有重疊區間。按起點排序後，依序合併：若當前與上一個重疊則合併，否則加入新區間。
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= out[-1][1]:
                out[-1][1] = max(out[-1][1], e)
            else:
                out.append([s, e])
        return out
```

## 複雜度分析

- **時間複雜度:** O(n log n)。
- **空間複雜度:** O(1) 額外（不含輸出）。
