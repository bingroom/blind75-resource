# Move Zeroes

**Topic:** Array
- **LeetCode 連結:** [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- **難度:** Easy

## 題目描述

給定一個整數陣列，將所有 0 移動到陣列末尾，同時保持非零元素的相對順序。需原地操作。

## 解題思路

1. 使用雙指標，write 指標指向下一個應放置非零元素的位置。
2. 遍歷陣列，遇到非零元素時與 write 位置交換。
3. write 指標前進，最終所有零自然被移到末尾。

## 程式碼

```python
# LeetCode 283. Move Zeroes
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two-pointer approach. `write` marks the position where the next
        non-zero element should be placed. After one pass, all non-zero
        elements are at the front in original order; fill the rest with 0.
        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
```

## 複雜度分析

- **時間複雜度:** O(n) -- single pass.
- **空間複雜度:** O(1) -- in-place swaps.
