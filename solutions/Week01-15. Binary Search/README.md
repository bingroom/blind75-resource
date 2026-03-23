# Binary Search

**Topic:** Binary Search

## Problem Description
Given a sorted array of integers `nums` and a target value, return the index of the target if found, otherwise return -1. The algorithm must run in O(log n) time.


## Solution

```python
# LeetCode 704. Binary Search
# Time: O(log n)  Space: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
```

## Approach
Standard binary search. Maintain `lo` and `hi` pointers. Compare the middle element to the target and halve the search space accordingly.

## Complexity
- **Time:** O(log n)
- **Space:** O(1)
