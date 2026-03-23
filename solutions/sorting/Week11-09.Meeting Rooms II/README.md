# Meeting Rooms II

## Problem Description
Given an array of meeting time intervals `[start, end]`, return the minimum number of conference rooms required.


## Solution

```python
# LeetCode 253. Meeting Rooms II
# Time: O(n log n)  Space: O(n)

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()  # sort by start time
        # Min-heap of end times (one entry per room in use)
        heap = [intervals[0][1]]

        for start, end in intervals[1:]:
            if start >= heap[0]:
                # Reuse the room that frees up earliest
                heapq.heapreplace(heap, end)
            else:
                # Need a new room
                heapq.heappush(heap, end)

        return len(heap)
```

## Approach
Sort by start time. Use a min-heap to track the end times of ongoing meetings. For each new meeting, if its start time is >= the earliest end time in the heap, reuse that room (pop and push the new end time). Otherwise, allocate a new room (push). The heap size at the end is the answer.

## Complexity
- **Time:** O(n log n)
- **Space:** O(n) for the heap
