# Bus Routes

- **LeetCode:** [815. Bus Routes](https://leetcode.com/problems/bus-routes/)

## Problem Description

Given a list of bus routes where `routes[i]` is the set of stops for bus `i`, find the minimum number of buses you must take to travel from `source` to `target`. You can switch buses at any shared stop. Return `-1` if impossible.

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
