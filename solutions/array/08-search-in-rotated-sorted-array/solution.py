# LeetCode 33. Search in Rotated Sorted Array
# 時間複雜度: O(log n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        在旋轉過的有序陣列（無重複）中找 target 的索引，沒有則回傳 -1。
        二分：先判斷左半或右半哪一段是有序的，再判斷 target 是否落在該段內。
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            # 左半 [lo..mid] 為有序
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # 右半 [mid..hi] 為有序
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
