# Find the Duplicate Number

**Topic:** Binary
- **LeetCode 連結:** [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
- **難度:** Medium

## 題目描述

給定一個包含 n+1 個整數的陣列，其中每個整數都在 1 到 n 之間，證明至少有一個重複數字。在不修改陣列且只用 O(1) 額外空間的前提下，找出該重複數字。

## 解題思路

1. 將每個值視為指向另一個索引的指標，形成隱式鏈結串列。
2. 使用 Floyd 龜兔賽跑演算法偵測環：快指標每次走兩步、慢指標走一步。
3. 當快慢指標相遇時，代表存在環。
4. 將慢指標重置到起點，兩指標同速前進，再次相遇點即為重複數字（環的入口）。

## 程式碼

```python
# LeetCode 287. Find the Duplicate Number
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Tortoise and Hare (cycle detection).
        Treat each value as a pointer to another index.
        Since there are n+1 values in range [1, n], a cycle must exist,
        and the entrance to the cycle is the duplicate number.
        """
        # Phase 1: detect the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the cycle entrance
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

## 複雜度分析

- **時間複雜度:** O(n) -- each phase is at most O(n).
- **空間複雜度:** O(1) -- only two pointers.
