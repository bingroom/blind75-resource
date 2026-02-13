# LeetCode 56. Merge Intervals
# 時間複雜度: O(n log n)  空間複雜度: O(1) 不含輸出
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合併所有重疊區間。按起點排序後，依序合併：若當前與上一個重疊則合併，否則加入新區間。
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= out[-1][1]:
                out[-1][1] = max(out[-1][1], e)
            else:
                out.append([s, e])
        return out
