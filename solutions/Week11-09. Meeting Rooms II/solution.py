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
