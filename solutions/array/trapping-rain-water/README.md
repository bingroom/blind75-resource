# Trapping Rain Water

- **LeetCode:** [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

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
