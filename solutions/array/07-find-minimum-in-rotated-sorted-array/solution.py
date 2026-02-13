# LeetCode 153. Find Minimum in Rotated Sorted Array
# 時間複雜度: O(log n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        旋轉過的有序陣列（無重複），找最小值。用二分搜：比較 mid 與 right 決定往左或往右。
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # 若 nums[mid] > nums[hi]，最小值在右半 (mid+1 ~ hi)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                # 否則在左半或就是 mid（含 mid）
                hi = mid
        return nums[lo]
