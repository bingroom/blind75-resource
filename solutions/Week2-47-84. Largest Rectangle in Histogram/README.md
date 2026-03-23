# Largest Rectangle in Histogram

**Topic:** Stack
- **LeetCode 連結:** [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- **難度:** Hard

## 題目描述

給定一個整數陣列表示柱狀圖中每根柱子的高度（寬度均為 1），求在該柱狀圖中能勾勒出的最大矩形面積。

## 解題思路

1. 使用單調遞增堆疊儲存柱子的索引。
2. 遍歷每根柱子，若當前柱子比堆疊頂端的柱子矮，則彈出並計算以彈出柱子高度為最大高度的矩形面積。
3. 彈出時將當前柱子的左邊界延伸至被彈出柱子的索引。
4. 遍歷結束後，處理堆疊中剩餘的柱子（它們可延伸到陣列末端）。
5. 過程中持續更新最大面積。

## 程式碼

```python
# LC 84. Largest Rectangle in Histogram (Hard)
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Monotonic stack approach

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # monotonic increasing stack of indices
        max_area = 0

        for i, h in enumerate(heights):
            # When current bar is shorter, pop and calculate areas
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx  # extend current bar's left boundary
            stack.append((start, h))

        # Process remaining bars that extend to the end
        n = len(heights)
        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))

        return max_area
```

## 複雜度分析

- **時間複雜度:** O(n) -- each bar is pushed and popped at most once
- **空間複雜度:** O(n)
