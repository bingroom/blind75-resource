# Cheapest Flights Within K Stops

**Topic:** Graph
- **LeetCode 連結:** [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- **難度:** Medium

## 題目描述

給定 n 個城市和航班資訊（起點、終點、價格），找出從起點到終點、最多經 k 站中轉的最便宜價格。

## 解題思路

1. 使用 Bellman-Ford 演算法，限制最多鬆弛 k+1 輪。
2. 初始化距離陣列，起點為 0，其餘為無限大。
3. 每輪遍歷所有航班，使用上一輪的距離值更新當前距離（避免同輪連鎖更新）。
4. 回傳終點的距離，若仍為無限大則回傳 -1。

## 程式碼

```python
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
```

## 複雜度分析

- **時間複雜度:** O(K * E) where E is the number of flights.
- **空間複雜度:** O(n) -- distance array (plus a copy each round).
