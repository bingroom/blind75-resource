# Task Scheduler

## Problem Description
Given a list of tasks represented by characters and a cooldown interval `n`, return the minimum number of intervals the CPU needs to finish all tasks. The same task must be separated by at least `n` intervals.

## Approach
The most frequent task dictates the schedule. Arrange the most frequent task in a grid with `(n + 1)` slots per row. The minimum time is `(max_freq - 1) * (n + 1) + max_count`, where `max_count` is how many tasks share the maximum frequency. The answer is the max of this and `len(tasks)` (when there are enough distinct tasks to fill all idle slots).

## Complexity
- **Time:** O(n) where n is the number of tasks
- **Space:** O(1) -- at most 26 task types
