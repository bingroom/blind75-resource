# Largest Rectangle in Histogram

## Problem Description
Given an array of integers representing the heights of bars in a histogram (each bar has width 1), find the area of the largest rectangle that can be formed.

## Approach
Use a monotonic increasing stack storing `(index, height)` pairs. For each bar, if it is shorter than the stack top, pop entries and compute the area each popped bar could form extending rightward to the current position. The popped bar's left boundary becomes the current bar's new start index (since the current bar can extend left through all popped shorter-or-equal bars). After iterating, remaining stack entries extend all the way to the right end. Track the maximum area throughout.

## Complexity
- **Time:** O(n) -- each bar is pushed and popped at most once
- **Space:** O(n)
