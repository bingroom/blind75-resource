# Container With Most Water

**Topic:** Array
- **LeetCode 連結:** [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- **難度:** Medium

## 題目描述

給定一個整數陣列 height，每個元素代表一條垂直線的高度。找出兩條線與 x 軸構成的容器，使其能容納最多的水，回傳最大容水量。

## 解題思路

1. 使用雙指標分別指向陣列的最左和最右端。
2. 計算當前兩指標之間的容水量：min(左高, 右高) * 寬度。
3. 移動較短那一側的指標（因為容水量受短邊限制，移動短邊才可能增大面積）。
4. 持續更新最大容水量，直到兩指標相遇。

## 程式碼

```python
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
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
