# LeetCode 15. 3Sum
# 時間複雜度: O(n²)  空間複雜度: O(1) 不含排序
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        找出所有和為 0 的三元組 (不重複)。排序 + 枚舉第一個數，其餘用雙指針做 2Sum。
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            # 避免重複：若與上一個數相同則跳過
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 在 i+1..n-1 之間用雙指針找兩數和 = -nums[i]
            lo, hi = i + 1, n - 1
            target = -nums[i]
            while lo < hi:
                s = nums[lo] + nums[hi]
                if s == target:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    # 跳過重複的 nums[lo]
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif s < target:
                    lo += 1
                else:
                    hi -= 1
        return ans
