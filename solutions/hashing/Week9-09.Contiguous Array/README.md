# Contiguous Array

- **LeetCode:** [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)

## Problem Description

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


## Solution

```python
# LeetCode 525. Contiguous Array
# Time: O(n)  Space: O(n)


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """
        Find the maximum length subarray with equal number of 0s and 1s.
        Treat 0 as -1, then the problem becomes finding the longest subarray
        with sum == 0, which is solved by prefix-sum + hash map.
        """
        # Map from prefix_sum -> earliest index where that sum occurred
        prefix = {0: -1}
        max_len = 0
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1

            if running_sum in prefix:
                # Subarray from prefix[running_sum]+1 to i has sum 0
                max_len = max(max_len, i - prefix[running_sum])
            else:
                prefix[running_sum] = i

        return max_len
```

## Approach

1. Replace every 0 with -1. Now the problem is: find the longest subarray whose sum is 0.
2. Maintain a running prefix sum and a hash map that records the **first** index at which each prefix sum was seen.
3. Seed the map with `{0: -1}` so that a subarray starting from index 0 is handled.
4. At each index `i`, if the current prefix sum was seen before at index `j`, then the subarray `[j+1 .. i]` sums to 0 (equal 0s and 1s). Update the maximum length.
5. Only store the first occurrence of each sum to maximize the subarray length.

## Complexity

- **Time:** O(n) — single pass through the array.
- **Space:** O(n) — hash map stores at most n+1 distinct prefix sums.
