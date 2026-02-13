# LeetCode 268. Missing Number
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        陣列含 n 個數，取值為 [0, n] 且不重複，找缺的那一個。
        法一：預期和 0+1+..+n = n*(n+1)//2，減去實際和即缺的數。
        """
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
