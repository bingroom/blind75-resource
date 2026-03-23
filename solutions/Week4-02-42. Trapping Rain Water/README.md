# Trapping Rain Water

**Topic:** Stack
- **LeetCode 連結:** [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- **難度:** Hard

## 題目描述

給定 n 個非負整數代表柱狀圖中每根柱子的高度（寬度為 1），計算下雨後能接住多少單位的雨水。

## 解題思路

1. 使用雙指標 left 和 right 分別從兩端向中間收攏。
2. 維護 left_max 和 right_max 記錄左右兩側目前遇過的最大高度。
3. 每次移動較矮一側的指標：若高度小於該側最大值，則累加差值（即可接的水量）；否則更新最大值。
4. 當兩指標相遇時結束，回傳總水量。

## 程式碼

```python
# LeetCode 42. Trapping Rain Water
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two-pointer approach.
        Water at any position = min(max_left, max_right) - height[i].
        Instead of precomputing both arrays, use two pointers converging
        inward. The smaller side determines the water level, because the
        taller side guarantees at least that much containment.
        """
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
```

## 複雜度分析

- **時間複雜度:** O(n) -- single pass with two pointers.
- **空間複雜度:** O(1) -- only a few variables.
