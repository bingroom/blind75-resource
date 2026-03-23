# First Bad Version

## Problem Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Given an API `isBadVersion(version)` which returns whether a version is bad, find the first bad version while minimizing the number of API calls.

## Approach
Classic binary search on a monotonic predicate. The versions form a sequence `[good, good, ..., bad, bad, ...]`. We binary search for the transition point: if `mid` is bad, the answer is at `mid` or to its left; if `mid` is good, the answer is to the right.

## Complexity
- **Time:** O(log n)
- **Space:** O(1)
