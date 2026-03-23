# Employee Free Time

**Topic:** Array
- **LeetCode 連結:** [759. Employee Free Time](https://leetcode.com/problems/employee-free-time/)
- **難度:** Hard

## 題目描述

給定多位員工各自的工作時間區間列表，找出所有員工共同的空閒時間區間。

## 解題思路

1. 將所有員工的工作區間合併為一個列表，並按起始時間排序。
2. 追蹤目前已見的最晚結束時間。
3. 若下一個區間的起始時間大於最晚結束時間，則產生一個空閒區間。
4. 更新最晚結束時間。

## 程式碼

```python
# LeetCode 759. Employee Free Time
# Time: O(n log n)  Space: O(n)


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten all intervals and sort by start time
        intervals = sorted(
            [iv for emp in schedule for iv in emp],
            key=lambda iv: iv.start
        )

        result = []
        # Track the latest end time seen so far
        end = intervals[0].end

        for iv in intervals[1:]:
            if iv.start > end:
                # Gap found between previous end and current start
                result.append(Interval(end, iv.start))
            end = max(end, iv.end)

        return result
```

## 複雜度分析

- **時間複雜度:** O(n log n) where n is total number of intervals
- **空間複雜度:** O(n)
