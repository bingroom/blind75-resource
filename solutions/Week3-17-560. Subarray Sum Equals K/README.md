# Subarray Sum Equals K

**Topic:** Array
- **LeetCode 連結:** [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- **難度:** Medium

## 題目描述

給定一個整數陣列和一個整數 k，計算和為 k 的連續子陣列數量。

## 解題思路

1. 使用前綴和搭配雜湊表記錄每個前綴和出現的次數。
2. 遍歷陣列，累計當前前綴和。
3. 檢查 (當前前綴和 - k) 在雜湊表中出現幾次，即為以當前位置結尾且和為 k 的子陣列數。
4. 將當前前綴和加入雜湊表。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) — single pass with O(1) hash map lookups.
- **空間複雜度:** O(n) — hash map stores at most n+1 distinct prefix sums.
