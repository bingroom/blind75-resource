# Next Permutation

**Topic:** Recursion
- **LeetCode 連結:** [31. Next Permutation](https://leetcode.com/problems/next-permutation/)
- **難度:** Medium

## 題目描述

給定一個整數陣列，將其重新排列為字典序中的下一個排列。若已是最大排列，則重排為最小排列。要求原地修改，不使用額外空間。

## 解題思路

1. 從右往左找到第一個 nums[i] < nums[i+1] 的位置 i（即「拐點」）。
2. 若找不到拐點，整個陣列為降序，直接反轉為升序即可。
3. 從右往左找到第一個大於 nums[i] 的元素，與 nums[i] 交換。
4. 將 i 之後的部分反轉為升序，得到下一個排列。

## 程式碼

```python
# LeetCode 31. Next Permutation
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        1. From the right, find the first index `i` where nums[i] < nums[i+1]
           (the "pivot"). Everything to the right of i is in descending order.
        2. Find the smallest element to the right of i that is larger than
           nums[i], swap them.
        3. Reverse the suffix after index i to get the smallest permutation
           of that suffix.
        If no pivot exists, the array is the last permutation -- reverse it
        to get the first.
        """
        n = len(nums)

        # Step 1: find the pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: find the successor to swap with
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## 複雜度分析

- **時間複雜度:** O(n) -- at most two linear scans plus one reverse.
- **空間複雜度:** O(1) -- all operations are in-place.
