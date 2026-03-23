# Sort Colors

**Topic:** Array
- **LeetCode 連結:** [75. Sort Colors](https://leetcode.com/problems/sort-colors/)
- **難度:** Medium

## 題目描述

給定一個包含紅色（0）、白色（1）、藍色（2）的陣列，將其原地排序使得相同顏色相鄰，且按紅、白、藍的順序排列。不可使用排序函式。

## 解題思路

1. 使用荷蘭國旗演算法，維護三個指標：lo、mid、hi。
2. 遇到 0 時，將 mid 與 lo 交換，lo 和 mid 都前進。
3. 遇到 1 時，mid 直接前進。
4. 遇到 2 時，將 mid 與 hi 交換，hi 後退，mid 不動（交換過來的元素尚未檢查）。
5. 當 mid 超過 hi 時結束。

## 程式碼

```python
# LeetCode 75. Sort Colors
# Time: O(n)  Space: O(1)
# Dutch National Flag algorithm

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort in-place using three pointers."""
        lo, mid, hi = 0, 0, len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
                # Don't advance mid -- swapped element needs inspection
```

## 複雜度分析

- **時間複雜度:** O(n) -- single pass
- **空間複雜度:** O(1)
