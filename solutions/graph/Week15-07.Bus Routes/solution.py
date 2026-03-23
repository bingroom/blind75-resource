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
