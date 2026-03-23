# Daily Temperatures

## Problem Description
Given an array of daily temperatures, return an array where each element is the number of days you have to wait until a warmer temperature. If there is no future warmer day, output 0.

## Approach
Use a monotonic decreasing stack that stores indices. For each new temperature, pop all stack entries with a smaller temperature -- each popped index has found its next warmer day at the current index. The difference in indices gives the wait time. Then push the current index onto the stack. Elements remaining on the stack after iteration have no warmer future day and stay 0.

## Complexity
- **Time:** O(n) -- each index is pushed and popped at most once
- **Space:** O(n)
