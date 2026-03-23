# First Bad Version

## Problem Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Given an API `isBadVersion(version)` which returns whether a version is bad, find the first bad version while minimizing the number of API calls.


## Solution

```python
# LeetCode 278. First Bad Version
# Time: O(log n)  Space: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid          # mid might be the first bad version
            else:
                lo = mid + 1      # mid is good, search right half
        return lo
```

## Approach
Classic binary search on a monotonic predicate. The versions form a sequence `[good, good, ..., bad, bad, ...]`. We binary search for the transition point: if `mid` is bad, the answer is at `mid` or to its left; if `mid` is good, the answer is to the right.

## Complexity
- **Time:** O(log n)
- **Space:** O(1)
