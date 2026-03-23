# Meeting Rooms II

## Problem Description
Given an array of meeting time intervals `[start, end]`, return the minimum number of conference rooms required.

## Approach
Sort by start time. Use a min-heap to track the end times of ongoing meetings. For each new meeting, if its start time is >= the earliest end time in the heap, reuse that room (pop and push the new end time). Otherwise, allocate a new room (push). The heap size at the end is the answer.

## Complexity
- **Time:** O(n log n)
- **Space:** O(n) for the heap
