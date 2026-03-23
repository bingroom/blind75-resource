# LeetCode 238. Product of Array Except Self
# 時間複雜度: O(n)  空間複雜度: O(1) 不含輸出陣列
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        回傳 output[i] = 除 nums[i] 外所有數的乘積。限制：不能用除法、盡量 O(1) 額外空間。
        做法：output[i] = (i 左邊所有數的乘積) * (i 右邊所有數的乘積)。
        先從左掃一遍填「左乘積」，再從右掃一遍乘上「右乘積」。
        """
        n = len(nums)
        out = [1] * n
        # 第一遍：out[i] = nums[0]*...*nums[i-1]（i 左邊的乘積）
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]
        # 第二遍：從右往左，乘上「右邊的乘積」
        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]
        return out
