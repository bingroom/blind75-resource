# Binary Search

## Problem Description
Given a sorted array of integers `nums` and a target value, return the index of the target if found, otherwise return -1. The algorithm must run in O(log n) time.

## Approach
Standard binary search. Maintain `lo` and `hi` pointers. Compare the middle element to the target and halve the search space accordingly.

## Complexity
- **Time:** O(log n)
- **Space:** O(1)
