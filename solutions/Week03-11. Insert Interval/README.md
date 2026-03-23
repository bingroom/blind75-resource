# Insert Interval

**Topic:** Array

- **LeetCode:** [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i^th` interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals`* after the insertion*.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

 

**Example 1:**

```

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

```

**Example 2:**

```

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

```

 

**Constraints:**

	- `0 <= intervals.length <= 10^4`

	- `intervals[i].length == 2`

	- `0 <= start_i <= end_i <= 10^5`

	- `intervals` is sorted by `start_i` in **ascending** order.

	- `newInterval.length == 2`

	- `0 <= start <= end <= 10^5`

## Solution

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

## 思路

- 左邊完全在 newInterval 前的直接加入；與 newInterval 有交集的區間合併成一個新区間；右邊完全在後的直接加入。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1) 額外（不含輸出）。

## 相關閱讀

- **演算法:** 區間合併、線性掃描
