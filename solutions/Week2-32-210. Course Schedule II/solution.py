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
