# LeetCode 57. Insert Interval
# 時間複雜度: O(n)  空間複雜度: O(1) 不含輸出
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        已排序無重疊區間，插入新区間並合併重疊。遍歷：與 newInterval 無交集的直接加入；有交集的合併成一個再繼續。
        """
        out = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        out.append(newInterval)
        while i < len(intervals):
            out.append(intervals[i])
            i += 1
        return out
