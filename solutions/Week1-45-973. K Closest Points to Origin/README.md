# K Closest Points to Origin

**Topic:** Heap
- **LeetCode 連結:** [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- **難度:** Medium

## 題目描述

給定一個二維平面上的點陣列 `points` 和一個整數 `k`，回傳距離原點 `(0, 0)` 最近的 `k` 個點。距離使用歐幾里得距離計算，結果順序不限。

## 解題思路

1. 使用大小為 `k` 的最大堆積（max-heap）來維護目前最近的 `k` 個點。
2. 遍歷每個點，計算其到原點的距離平方（取負值以模擬最大堆積）。
3. 若堆積大小不足 `k`，直接加入；若當前點比堆積頂端更近，則替換堆積頂端。
4. 遍歷結束後，堆積中的 `k` 個點即為答案。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n log k)
- **空間複雜度:** O(k)
