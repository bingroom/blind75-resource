# K Closest Points to Origin

**Topic:** Sorting

## Problem Description
Given an array of points on the X-Y plane and an integer k, return the k closest points to the origin (0, 0). Distance is Euclidean distance.


## Solution

```python
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
```

## Approach
Maintain a max-heap of size k (using negated distances with Python's min-heap). For each point, if the heap is smaller than k, push it in. Otherwise, if the point is closer than the farthest in the heap, replace the top.

## Complexity
- **Time:** O(n log k)
- **Space:** O(k)
