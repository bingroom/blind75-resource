# Meeting Rooms

## Problem Description
Given an array of meeting time intervals `[start, end]`, determine if a person could attend all meetings (i.e., no two meetings overlap).

## Approach
Sort intervals by start time. Check each consecutive pair: if any meeting starts before the previous one ends, there is an overlap.

## Complexity
- **Time:** O(n log n) for sorting
- **Space:** O(1) ignoring sort space
