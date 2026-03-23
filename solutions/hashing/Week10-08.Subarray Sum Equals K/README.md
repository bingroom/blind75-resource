# Subarray Sum Equals K

- **LeetCode:** [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

## Problem Description

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.


## Solution

```python
# LeetCode 560. Subarray Sum Equals K
# Time: O(n)  Space: O(n)

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Count subarrays whose elements sum to k using prefix-sum + hash map.
        If prefix[i] - prefix[j] == k, then subarray (j, i] sums to k.
        """
        count = 0
        running_sum = 0
        # Map from prefix_sum -> number of times it has occurred
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # empty prefix

        for num in nums:
            running_sum += num
            # How many earlier prefixes equal running_sum - k?
            count += prefix_counts[running_sum - k]
            prefix_counts[running_sum] += 1

        return count
```

## Approach

1. Maintain a running prefix sum and a hash map that counts how many times each prefix sum has appeared.
2. Initialize the map with `{0: 1}` to account for subarrays starting at index 0.
3. At each index, compute the running sum. The number of subarrays ending here with sum `k` equals the number of earlier prefixes with value `running_sum - k` (because `prefix[i] - prefix[j] == k` means the subarray `(j, i]` sums to `k`).
4. Look up `running_sum - k` in the map and add its count to the answer. Then record the current prefix sum.

## Complexity

- **Time:** O(n) — single pass with O(1) hash map lookups.
- **Space:** O(n) — hash map stores at most n+1 distinct prefix sums.
