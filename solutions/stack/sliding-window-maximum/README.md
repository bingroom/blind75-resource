# Sliding Window Maximum

## Problem Description
Given an array of integers and a sliding window of size k moving from left to right, return the maximum value in each window position.

## Approach
Use a monotonic decreasing deque that stores indices. For each new element: (1) remove the front index if it has fallen outside the window, (2) remove all back indices whose values are less than or equal to the current element (they can never be the maximum while the current element is in the window), (3) append the current index. The front of the deque always holds the index of the maximum in the current window. Start collecting results once the first full window is formed (i >= k - 1).

## Complexity
- **Time:** O(n) -- each element is added and removed from the deque at most once
- **Space:** O(k) for the deque
