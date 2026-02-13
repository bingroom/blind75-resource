# LeetCode 1. Two Sum
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        在陣列中找兩數之和等於 target，回傳兩數的索引。
        使用 Hash Map 一次遍歷：邊走邊查「target - 當前值」是否已出現。
        """
        # seen[數值] = 索引，用來 O(1) 查詢「互補數」是否出現過
        seen = {}
        for i, x in enumerate(nums):
            # 互補數 = target - 當前數，若在 seen 裡表示之前已出現過
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
