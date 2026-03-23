# Employee Free Time

## Problem Description
Given a list of schedules for multiple employees (each schedule is a list of non-overlapping intervals sorted by start time), return the list of finite intervals representing the common free time for all employees.


## Solution

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

## Approach
Flatten all intervals from all employees, sort by start time, then merge. Whenever the next interval starts after the current merged end, that gap is a free-time interval.

## Complexity
- **Time:** O(n log n) where n is total number of intervals
- **Space:** O(n)
