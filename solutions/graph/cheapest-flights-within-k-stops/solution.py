# LeetCode 787. Cheapest Flights Within K Stops
# Time: O(K * E)  Space: O(n)
# Bellman-Ford limited to K+1 relaxation rounds

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dist[i] = cheapest cost to reach node i from src
        dist = [float("inf")] * n
        dist[src] = 0

        # At most k stops means at most k+1 edges
        for _ in range(k + 1):
            # Copy to avoid using updated values within the same round
            prev = dist[:]
            for u, v, w in flights:
                if prev[u] + w < dist[v]:
                    dist[v] = prev[u] + w

        return dist[dst] if dist[dst] != float("inf") else -1
