# Course Schedule II

**Topic:** Graph

- **LeetCode:** [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

## Problem Description

There are `numCourses` courses labeled `0` to `numCourses - 1`. Given an array `prerequisites` where `prerequisites[i] = [a, b]` means you must take course `b` before course `a`, return a valid ordering of courses to finish all of them. If impossible, return an empty array.


## Solution

```python
# LeetCode 210. Course Schedule II
# Time: O(V + E)  Space: O(V + E)
# Topological sort via Kahn's algorithm (BFS)

from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Start with all courses that have no prerequisites
        q = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return order if len(order) == numCourses else []
```

## Approach

Topological sort using Kahn's algorithm (BFS):

1. Build an adjacency list and compute in-degrees for every course.
2. Enqueue all courses with in-degree 0 (no prerequisites).
3. Process the queue: for each dequeued course, add it to the result and decrement in-degrees of its dependents. Enqueue any dependent whose in-degree drops to 0.
4. If the result contains all courses, return it; otherwise a cycle exists, so return an empty list.

## Complexity

- **Time:** O(V + E) where V = numCourses and E = number of prerequisites.
- **Space:** O(V + E) -- adjacency list and in-degree array.
