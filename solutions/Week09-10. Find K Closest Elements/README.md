# Find K Closest Elements

**Topic:** Array

- **LeetCode:** [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

## Problem Description

Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should be sorted in ascending order. An integer `a` is closer to `x` than `b` if `|a - x| < |b - x|`, or `|a - x| == |b - x|` and `a < b`.


## Solution

```python
# LeetCode 658. Find K Closest Elements
# Time: O(log(n - k) + k)  Space: O(1) excluding output

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary search for the left boundary of the k-length window.
        The window starts at some index in [0, n - k]. For a candidate
        start `mid`, compare the distance of arr[mid] and arr[mid + k]
        to x: if arr[mid + k] is closer (or equal), shift right.
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # Compare which side is farther from x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
```

## Approach

Use **binary search** on the starting index of the result window:

1. The answer is a contiguous window of size `k`. Its start index lies in `[0, n - k]`.
2. Binary search for the optimal start. At each `mid`, compare the distance of `arr[mid]` (left edge) and `arr[mid + k]` (one past the right edge) to `x`.
3. If `x - arr[mid] > arr[mid + k] - x`, the window should shift right (`left = mid + 1`); otherwise shift left (`right = mid`).
4. Return `arr[left:left + k]`.

## Complexity

- **Time:** O(log(n - k) + k) -- binary search plus slicing the result.
- **Space:** O(1) -- excluding the output list.
