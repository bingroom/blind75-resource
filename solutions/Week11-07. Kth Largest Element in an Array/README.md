# Kth Largest Element in an Array

**Topic:** Sorting

## Problem Description
Given an integer array `nums` and an integer `k`, return the kth largest element. Note that it is the kth largest in sorted order, not the kth distinct element.


## Solution

```python
# LeetCode 215. Kth Largest Element in an Array
# Time: O(n log k)  Space: O(k)

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```

## Approach
Quickselect algorithm: partition the array around a random pivot. If the pivot lands at position `n - k`, we found the answer. Otherwise, recurse into the half that contains the target index.

## Complexity
- **Time:** O(n) average, O(n^2) worst case
- **Space:** O(1) extra space (in-place partitioning, tail recursion)
