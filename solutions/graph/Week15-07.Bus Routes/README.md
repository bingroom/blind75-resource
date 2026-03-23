# Bus Routes

- **LeetCode:** [815. Bus Routes](https://leetcode.com/problems/bus-routes/)

## Problem Description

Given a list of bus routes where `routes[i]` is the set of stops for bus `i`, find the minimum number of buses you must take to travel from `source` to `target`. You can switch buses at any shared stop. Return `-1` if impossible.


## Solution

```python
# LeetCode 815. Bus Routes
# Time: O(N * M)  Space: O(N * M)
# BFS on routes (N = number of routes, M = max stops per route)

from typing import List
from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Map each stop to the list of route indices that serve it
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        # BFS over routes: start from all routes containing the source
        visited_routes = set()
        visited_stops = {source}
        q = deque()

        for route_idx in stop_to_routes[source]:
            visited_routes.add(route_idx)
            q.append((route_idx, 1))

        while q:
            route_idx, buses = q.popleft()
            for stop in routes[route_idx]:
                if stop == target:
                    return buses
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_route in stop_to_routes[stop]:
                        if next_route not in visited_routes:
                            visited_routes.add(next_route)
                            q.append((next_route, buses + 1))

        return -1
```

## Approach

BFS at the route level:

1. Build a mapping from each stop to the set of routes that serve it.
2. Start BFS from all routes that contain the `source` stop (1 bus each).
3. For each route in the queue, iterate through its stops. If a stop equals `target`, return the bus count. Otherwise, for each unvisited stop, enqueue all unvisited routes that serve that stop (with bus count + 1).
4. Track visited routes and stops to avoid reprocessing.

The key insight is performing BFS on routes rather than individual stops, which reduces the search space.

## Complexity

- **Time:** O(N * M) where N is the number of routes and M is the average number of stops per route.
- **Space:** O(N * M) -- stop-to-route mapping and visited sets.
