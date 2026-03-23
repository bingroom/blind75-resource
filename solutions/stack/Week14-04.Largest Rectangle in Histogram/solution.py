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
