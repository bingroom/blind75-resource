# Largest Rectangle in Histogram

## Problem Description
Given an array of integers representing the heights of bars in a histogram (each bar has width 1), find the area of the largest rectangle that can be formed.


## Solution

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

## Approach
Use a monotonic increasing stack storing `(index, height)` pairs. For each bar, if it is shorter than the stack top, pop entries and compute the area each popped bar could form extending rightward to the current position. The popped bar's left boundary becomes the current bar's new start index (since the current bar can extend left through all popped shorter-or-equal bars). After iterating, remaining stack entries extend all the way to the right end. Track the maximum area throughout.

## Complexity
- **Time:** O(n) -- each bar is pushed and popped at most once
- **Space:** O(n)
