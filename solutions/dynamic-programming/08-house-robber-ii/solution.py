# LeetCode 213. House Robber II (環狀)
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        房子排成環，相鄰不能偷。拆成兩段線性：不偷第一間、不偷最後一間，取兩次 House Robber I 的較大值。
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_range(arr: List[int]) -> int:
            prev, cur = 0, arr[0]
            for i in range(1, len(arr)):
                prev, cur = cur, max(cur, prev + arr[i])
            return cur

        return max(rob_range(nums[:-1]), rob_range(nums[1:]))
