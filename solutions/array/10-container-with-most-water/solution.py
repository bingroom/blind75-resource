# LeetCode 11. Container With Most Water
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        兩條垂直線與 x 軸圍成容器，容量 = min(height[i], height[j]) * (j - i)。
        雙指針：從兩端往內，每次移動較短的那邊（因為容量由短邊決定）。
        """
        lo, hi = 0, len(height) - 1
        best = 0
        while lo < hi:
            w = hi - lo
            h = min(height[lo], height[hi])
            best = max(best, w * h)
            # 移動較短的一邊才有機會變大
            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
        return best
