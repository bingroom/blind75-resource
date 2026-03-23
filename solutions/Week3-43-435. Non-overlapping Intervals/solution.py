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
