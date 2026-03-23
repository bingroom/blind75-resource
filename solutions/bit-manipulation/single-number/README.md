# Single Number

## Problem Description
Given a non-empty array of integers where every element appears twice except for one, find that single element. The solution must use constant extra space.

## Approach
XOR all elements together. Since `a ^ a = 0` and `a ^ 0 = a`, all pairs cancel out, leaving only the unique number.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
