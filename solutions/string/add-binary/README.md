# Add Binary

## Problem Description
Given two binary strings `a` and `b`, return their sum as a binary string.

## Approach
Simulate binary addition from right to left, tracking the carry. Process both strings simultaneously, appending each bit of the result. Reverse at the end.

## Complexity
- **Time:** O(max(m, n))
- **Space:** O(max(m, n)) for the result
