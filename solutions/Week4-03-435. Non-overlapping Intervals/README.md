# Non-overlapping Intervals

**Topic:** Array
- **LeetCode 連結:** [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- **難度:** Medium

## 題目描述

給定一組區間，計算最少需要移除幾個區間，使剩餘區間兩兩不重疊。

## 解題思路

1. 按區間的右端點排序。
2. 貪心選擇：依序選取結束時間最早且不與已選區間重疊的區間。
3. 計算最多能保留的不重疊區間數。
4. 總數減去保留數即為需移除的最少區間數。

## 程式碼

```python
# LeetCode 435. Non-overlapping Intervals
# 時間複雜度: O(n log n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        求最少移除幾個區間可使剩餘區間兩兩不重疊。等價於求「最多保留幾個不重疊區間」，按右端排序後貪心取。
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 1
        end = intervals[0][1]
        for s, e in intervals[1:]:
            if s >= end:
                count += 1
                end = e
        return len(intervals) - count
```

## 複雜度分析

- **時間複雜度:** O(n log n)。
- **空間複雜度:** O(1)。
