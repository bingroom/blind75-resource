# LeetCode 128. Longest Consecutive Sequence
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        求未排序陣列中最長連續數字序列的長度（如 1,2,3,4）。用 set 存所有數，只從「序列起點」開始數長度。
        """
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                cur = x
                while cur in s:
                    cur += 1
                best = max(best, cur - x)
        return best
