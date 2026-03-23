# Merge Intervals

- **LeetCode:** [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

 

**Example 1:**

```

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

```

**Example 2:**

```

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

```

**Example 3:**

```

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

```

 

**Constraints:**

	- `1 <= intervals.length <= 10^4`

	- `intervals[i].length == 2`

	- `0 <= start_i <= end_i <= 10^4`

## Solution

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

## 思路

- **排序 + 線性掃描：** 按區間起點排序，遍歷時若當前區間與結果中最後一個重疊則合併（更新右端），否則加入新區間。

## 時間 / 空間複雜度

- **時間:** O(n log n)。
- **空間:** O(1) 額外（不含輸出）。

## 相關閱讀

- **演算法:** 區間排序、合併
