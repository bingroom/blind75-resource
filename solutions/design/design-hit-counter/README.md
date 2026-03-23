# Design Hit Counter

## Problem Description
Design a hit counter that counts the number of hits received in the past 5 minutes (300 seconds). Each function accepts a timestamp parameter (in seconds granularity) and calls are made in chronological order.

## Approach
Use a queue to store hit timestamps. On `getHits`, pop all timestamps older than `timestamp - 300` from the front, then return the queue length. Since timestamps are monotonically increasing, old entries are always at the front.

## Complexity
- **Time:** O(1) amortized for `hit`, O(n) worst case for `getHits` (but each element is popped at most once)
- **Space:** O(n) where n is the number of hits in the last 300 seconds
