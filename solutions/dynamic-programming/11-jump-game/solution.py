# LeetCode 55. Jump Game
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        從索引 0 出發，nums[i] 為可跳最遠步數，能否到達最後一格。維護「最遠可達索引」即可。
        """
        reach = 0
        for i, x in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + x)
        return True
