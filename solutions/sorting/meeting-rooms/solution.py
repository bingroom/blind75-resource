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
