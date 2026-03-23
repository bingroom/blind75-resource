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
