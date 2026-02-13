# LeetCode 217. Contains Duplicate
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        判斷陣列中是否有重複元素。
        用 set 記錄已見過的數，遇過就回傳 True。
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
