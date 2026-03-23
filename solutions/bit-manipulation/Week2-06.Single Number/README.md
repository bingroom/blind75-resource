# Single Number

## Problem Description
Given a non-empty array of integers where every element appears twice except for one, find that single element. The solution must use constant extra space.


## Solution

```python
# LeetCode 136. Single Number
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR cancels out pairs, leaving the single number
        return result
```

## Approach
XOR all elements together. Since `a ^ a = 0` and `a ^ 0 = a`, all pairs cancel out, leaving only the unique number.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
