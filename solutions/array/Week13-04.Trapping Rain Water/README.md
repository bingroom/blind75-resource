# Trapping Rain Water

- **LeetCode:** [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


## Solution

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

## Approach

**Two-pointer** technique:

1. Water above position `i` equals `min(max_left, max_right) - height[i]`.
2. Use two pointers at the ends, tracking `left_max` and `right_max`.
3. Process the side with the shorter max height, because the other side guarantees at least that much containment:
   - If `height[left] < height[right]`: the left side is the bottleneck. Update `left_max` or add `left_max - height[left]` to the answer.
   - Otherwise: process the right side symmetrically.
4. Move the processed pointer inward. Repeat until the pointers meet.

## Complexity

- **Time:** O(n) -- single pass with two pointers.
- **Space:** O(1) -- only a few variables.
