# LeetCode 53. Maximum Subarray (Kadane's Algorithm)
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        求連續子陣列的最大和（至少取一個元素）。
        Kadane：以「以當前位置結尾」的最大和來推，要麼接上前面，要麼只取自己。
        """
        if not nums:
            return 0
        # cur = 以當前位置為結尾的最大子陣列和
        cur = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            # 要麼接上前面 (cur + nums[i])，要麼從這裡重新開始 (nums[i])
            cur = max(nums[i], cur + nums[i])
            best = max(best, cur)
        return best
