# LeetCode 973. K Closest Points to Origin
# Time: O(n log k)  Space: O(k)

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max-heap of size k (negate distances since heapq is a min-heap)
        heap = []
        for x, y in points:
            dist = -(x * x + y * y)
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, x, y))

        return [[x, y] for _, x, y in heap]
