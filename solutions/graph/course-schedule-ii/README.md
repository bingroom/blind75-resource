# Course Schedule II

- **LeetCode:** [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

## Problem Description

There are `numCourses` courses labeled `0` to `numCourses - 1`. Given an array `prerequisites` where `prerequisites[i] = [a, b]` means you must take course `b` before course `a`, return a valid ordering of courses to finish all of them. If impossible, return an empty array.

## Approach

Topological sort using Kahn's algorithm (BFS):

1. Build an adjacency list and compute in-degrees for every course.
2. Enqueue all courses with in-degree 0 (no prerequisites).
3. Process the queue: for each dequeued course, add it to the result and decrement in-degrees of its dependents. Enqueue any dependent whose in-degree drops to 0.
4. If the result contains all courses, return it; otherwise a cycle exists, so return an empty list.

## Complexity

- **Time:** O(V + E) where V = numCourses and E = number of prerequisites.
- **Space:** O(V + E) -- adjacency list and in-degree array.
