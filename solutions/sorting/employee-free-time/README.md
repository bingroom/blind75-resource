# Employee Free Time

## Problem Description
Given a list of schedules for multiple employees (each schedule is a list of non-overlapping intervals sorted by start time), return the list of finite intervals representing the common free time for all employees.

## Approach
Flatten all intervals from all employees, sort by start time, then merge. Whenever the next interval starts after the current merged end, that gap is a free-time interval.

## Complexity
- **Time:** O(n log n) where n is total number of intervals
- **Space:** O(n)
