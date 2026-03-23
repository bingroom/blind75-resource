# Smallest Range Covering Elements from K Lists

**Topic:** Heap
- **LeetCode 連結:** [632. Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)
- **難度:** Hard

## 題目描述

給定 k 個各自升序排列的整數列表，找出包含每個列表至少一個元素的最小範圍 [a, b]。

## 解題思路

1. 使用最小堆，初始放入每個列表的第一個元素，同時追蹤當前最大值。
2. 當前範圍為 [堆頂最小值, 當前最大值]，若更小則更新答案。
3. 彈出最小元素，從該元素所屬列表推入下一個元素，更新最大值。
4. 當某列表耗盡時停止，因為無法再覆蓋所有列表。

## 程式碼

```python
# LeetCode 632. Smallest Range Covering Elements from K Lists
# Time: O(n log k)  Space: O(k)

import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min-heap: (value, list_index, element_index)
        heap = []
        current_max = float('-inf')

        # Initialize with the first element from each list
        for i, row in enumerate(nums):
            heapq.heappush(heap, (row[0], i, 0))
            current_max = max(current_max, row[0])

        best = [heap[0][0], current_max]

        while True:
            val, list_idx, elem_idx = heapq.heappop(heap)

            # Try to advance in the list we just popped from
            if elem_idx + 1 == len(nums[list_idx]):
                break  # one list exhausted, can't cover all k lists anymore

            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)

            # Current range is [heap[0][0], current_max]
            if current_max - heap[0][0] < best[1] - best[0]:
                best = [heap[0][0], current_max]

        return best
```

## 複雜度分析

- **時間複雜度:** O(n log k) where n is total elements across all lists
- **空間複雜度:** O(k) for the heap
