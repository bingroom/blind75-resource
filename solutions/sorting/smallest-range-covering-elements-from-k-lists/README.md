# Smallest Range Covering Elements from K Lists

## Problem Description
Given k sorted lists of integers, find the smallest range `[a, b]` that includes at least one number from each of the k lists.

## Approach
Use a min-heap to maintain one element from each list. Track the current maximum. The range is `[heap_min, current_max]`. Pop the minimum element and advance in its list, updating the max and checking for a smaller range. Stop when any list is exhausted.

## Complexity
- **Time:** O(n log k) where n is total elements across all lists
- **Space:** O(k) for the heap
