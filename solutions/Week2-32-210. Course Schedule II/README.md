# Course Schedule II

**Topic:** Graph
- **LeetCode 連結:** [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- **難度:** Medium

## 題目描述

給定課程總數和先修關係，回傳完成所有課程的修課順序。若無法完成所有課程（存在環），則回傳空陣列。

## 解題思路

1. 建立鄰接表和入度陣列。
2. 將所有入度為 0 的課程（無先修條件）加入佇列。
3. 每次從佇列取出一門課程加入結果，並將其鄰居的入度減 1。
4. 若鄰居入度降為 0，加入佇列。
5. 若結果長度等於課程總數，回傳結果；否則存在環，回傳空陣列。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(V + E) where V = numCourses and E = number of prerequisites.
- **空間複雜度:** O(V + E) -- adjacency list and in-degree array.
