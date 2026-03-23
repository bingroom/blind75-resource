# LeetCode 300. Longest Increasing Subsequence
# 時間複雜度: O(n²) 或 O(n log n) 二分  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        求最長嚴格遞增子序列長度。法二：維護「長度為 i 的 LIS 最小結尾」的陣列，用二分插入。
        """
        tails = []
        for x in nums:
            i = bisect.bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)
