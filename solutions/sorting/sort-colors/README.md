# Sort Colors

## Problem Description
Given an array `nums` with n objects colored red (0), white (1), or blue (2), sort them in-place so that objects of the same color are adjacent, in the order 0, 1, 2. Do not use the library sort function.

## Approach
Dutch National Flag algorithm with three pointers: `lo` (boundary for 0s), `mid` (current element), `hi` (boundary for 2s). Swap 0s to the front, 2s to the back, and skip 1s.

## Complexity
- **Time:** O(n) -- single pass
- **Space:** O(1)
