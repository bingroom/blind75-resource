# Meeting Rooms II

**Topic:** Array
- **LeetCode 連結:** [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- **難度:** Medium

## 題目描述

給定一組會議的起止時間區間，計算同時進行的會議最多需要幾間會議室。

## 解題思路

1. 按開始時間排序所有會議。
2. 使用最小堆維護各會議室的結束時間。
3. 對每場會議，若開始時間不早於堆頂（最早結束），可重用該會議室。
4. 否則需要新增一間會議室，最終堆的大小即為答案。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n log n)
- **空間複雜度:** O(n) for the heap
