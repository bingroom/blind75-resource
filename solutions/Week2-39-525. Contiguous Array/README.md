# Contiguous Array

**Topic:** Array
- **LeetCode 連結:** [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)
- **難度:** Medium

## 題目描述

給定一個只包含 0 和 1 的二元陣列，找出含有相同數量 0 和 1 的最長連續子陣列的長度。

## 解題思路

1. 將 0 視為 -1，問題轉化為找最長和為 0 的子陣列。
2. 使用前綴和搭配雜湊表，記錄每個前綴和第一次出現的索引。
3. 遍歷陣列，遇到 1 則前綴和 +1，遇到 0 則 -1。
4. 若相同的前綴和之前出現過，則兩次之間的子陣列和為 0，更新最大長度。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) — single pass through the array.
- **空間複雜度:** O(n) — hash map stores at most n+1 distinct prefix sums.
