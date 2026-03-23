# First Missing Positive

**Topic:** Hash Table
- **LeetCode 連結:** [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
- **難度:** Hard

## 題目描述

給定一個未排序的整數陣列，找出缺少的最小正整數。要求時間 O(n)、空間 O(1)。

## 解題思路

1. 答案必在 [1, n+1] 範圍內。
2. 使用原地交換（循環排序）：將值 v 放到索引 v-1 的位置。
3. 遍歷陣列，對每個元素不斷交換到正確位置。
4. 再次遍歷，第一個 nums[i] != i+1 的位置即為答案。

## 程式碼

```python
# LeetCode 41. First Missing Positive
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Index-marking (cyclic sort) approach.
        The answer must be in [1, n+1]. Place each value v in nums[v-1]
        by swapping. After placement, the first index i where
        nums[i] != i + 1 gives the answer.
        """
        n = len(nums)

        # Place each number at its "correct" index: value v -> index v-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] into its correct position
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        # The first position where nums[i] != i + 1 is the answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
```

## 複雜度分析

- **時間複雜度:** O(n) -- each element moves to its final position at most once.
- **空間複雜度:** O(1) -- rearrangement is done in-place.
