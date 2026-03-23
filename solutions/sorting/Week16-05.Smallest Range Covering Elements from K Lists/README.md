# Smallest Range Covering Elements from K Lists

## Problem Description
Given k sorted lists of integers, find the smallest range `[a, b]` that includes at least one number from each of the k lists.


## Solution

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

## Approach
Use a min-heap to maintain one element from each list. Track the current maximum. The range is `[heap_min, current_max]`. Pop the minimum element and advance in its list, updating the max and checking for a smaller range. Stop when any list is exhausted.

## Complexity
- **Time:** O(n log k) where n is total elements across all lists
- **Space:** O(k) for the heap
