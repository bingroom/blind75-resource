# Non-overlapping Intervals

**Topic:** Greedy

- **LeetCode:** [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return *the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping*.

**Note** that intervals which only touch at a point are **non-overlapping**. For example, `[1, 2]` and `[2, 3]` are non-overlapping.

 

**Example 1:**

```

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

```

**Example 2:**

```

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

```

**Example 3:**

```

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

```

 

**Constraints:**

	- `1 <= intervals.length <= 10^5`

	- `intervals[i].length == 2`

	- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Solution

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

## 思路

- **等價於「最多保留幾個不重疊區間」：** 按區間**右端**排序，貪心取：每次取與當前 end 不重疊且右端盡量小的區間。答案 = 總數 - 保留數。

## 時間 / 空間複雜度

- **時間:** O(n log n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Greedy、區間調度
