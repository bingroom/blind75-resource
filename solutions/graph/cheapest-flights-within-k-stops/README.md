# Cheapest Flights Within K Stops

- **LeetCode:** [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Problem Description

There are `n` cities connected by flights. Given `flights[i] = [from, to, price]`, find the cheapest price from `src` to `dst` with at most `k` stops. Return `-1` if no such route exists.

## Approach

Bellman-Ford with a limit of `k + 1` relaxation rounds:

1. Initialize distances: `dist[src] = 0`, all others `inf`.
2. Run `k + 1` rounds of edge relaxation. In each round, snapshot the current distances to prevent cascading updates within the same round (which would allow more stops than permitted).
3. After all rounds, `dist[dst]` holds the answer if reachable, else return -1.

Using a snapshot of the previous round's distances is the key insight -- it ensures each round adds at most one edge (one stop) to any path.

## Complexity

- **Time:** O(K * E) where E is the number of flights.
- **Space:** O(n) -- distance array (plus a copy each round).
