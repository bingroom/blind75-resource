# Rotate Array

**Topic:** Array
- **LeetCode 連結:** [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- **難度:** Medium

## 題目描述

給定一個整數陣列，將陣列中的元素向右輪轉 k 個位置。要求原地修改，使用 O(1) 額外空間。

## 解題思路

1. 先將 k 取餘數（k %= n），處理 k 大於陣列長度的情況。
2. 反轉整個陣列。
3. 反轉前 k 個元素。
4. 反轉剩餘的 n-k 個元素，即可得到向右輪轉 k 位的結果。

## 程式碼

```python
# LeetCode 189. Rotate Array
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Three-reverse approach:
        To rotate right by k, reverse the whole array, then reverse
        the first k elements, then reverse the rest.
        Example: [1,2,3,4,5,6,7], k=3
          reverse all:   [7,6,5,4,3,2,1]
          reverse [0:3]: [5,6,7,4,3,2,1]
          reverse [3:]:  [5,6,7,1,2,3,4]
        """
        n = len(nums)
        k %= n  # handle k > n

        def reverse(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

## 複雜度分析

- **時間複雜度:** O(n) -- three passes, each at most O(n).
- **空間複雜度:** O(1) -- in-place swaps only.
