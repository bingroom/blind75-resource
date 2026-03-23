# Bus Routes

**Topic:** Graph
- **LeetCode 連結:** [815. Bus Routes](https://leetcode.com/problems/bus-routes/)
- **難度:** Hard

## 題目描述

給定多條公車路線（每條路線包含多個站點），從起始站到目標站最少需要搭幾趟公車。

## 解題思路

1. 建立站點到路線的映射表。
2. 從起始站所在的所有路線開始 BFS。
3. 對每條路線的每個站點，若到達目標站則回傳搭乘次數。
4. 將未訪問的路線加入佇列繼續搜尋。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(N * M) where N is the number of routes and M is the average number of stops per route.
- **空間複雜度:** O(N * M) -- stop-to-route mapping and visited sets.
