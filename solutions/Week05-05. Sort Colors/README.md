# Sort Colors

**Topic:** Sorting

## Problem Description
Given an array `nums` with n objects colored red (0), white (1), or blue (2), sort them in-place so that objects of the same color are adjacent, in the order 0, 1, 2. Do not use the library sort function.


## Solution

```python
# LeetCode 75. Sort Colors
# Time: O(n)  Space: O(1)
# Dutch National Flag algorithm

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort in-place using three pointers."""
        lo, mid, hi = 0, 0, len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
                # Don't advance mid -- swapped element needs inspection
```

## Approach
Dutch National Flag algorithm with three pointers: `lo` (boundary for 0s), `mid` (current element), `hi` (boundary for 2s). Swap 0s to the front, 2s to the back, and skip 1s.

## Complexity
- **Time:** O(n) -- single pass
- **Space:** O(1)
