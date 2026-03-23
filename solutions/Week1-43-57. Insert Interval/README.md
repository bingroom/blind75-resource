# Insert Interval

**Topic:** Array
- **LeetCode 連結:** [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
- **難度:** Medium

## 題目描述

給定一組已排序且不重疊的區間 `intervals`，以及一個新區間 `newInterval`，將新區間插入並合併所有重疊的區間，回傳合併後仍排序且不重疊的區間列表。

## 解題思路

1. 將所有結束時間小於新區間起始時間的區間直接加入結果（無交集，在左邊）。
2. 將所有與新區間重疊的區間合併：更新新區間的起始和結束時間為兩者的最小起始和最大結束。
3. 將合併後的新區間加入結果。
4. 將剩餘的區間直接加入結果（無交集，在右邊）。

## 程式碼

```python
# LeetCode 57. Insert Interval
# 時間複雜度: O(n)  空間複雜度: O(1) 不含輸出
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        已排序無重疊區間，插入新区間並合併重疊。遍歷：與 newInterval 無交集的直接加入；有交集的合併成一個再繼續。
        """
        out = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        out.append(newInterval)
        while i < len(intervals):
            out.append(intervals[i])
            i += 1
        return out
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1) 額外（不含輸出）。
