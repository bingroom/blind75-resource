# Meeting Rooms

## Problem Description
Given an array of meeting time intervals `[start, end]`, determine if a person could attend all meetings (i.e., no two meetings overlap).


## Solution

```python
# LeetCode 252. Meeting Rooms
# Time: O(n log n)  Space: O(1)

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False  # overlap found
        return True
```

## Approach
Sort intervals by start time. Check each consecutive pair: if any meeting starts before the previous one ends, there is an overlap.

## Complexity
- **Time:** O(n log n) for sorting
- **Space:** O(1) ignoring sort space
