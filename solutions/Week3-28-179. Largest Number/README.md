# Largest Number

**Topic:** String
- **LeetCode 連結:** [179. Largest Number](https://leetcode.com/problems/largest-number/)
- **難度:** Medium

## 題目描述

給定一組非負整數，將它們排列成最大的數字並以字串回傳。

## 解題思路

1. 將所有數字轉為字串。
2. 自訂比較函式：比較 a+b 與 b+a 的字串大小。
3. 按此規則降序排序後串接所有字串。
4. 處理全零的邊界情況。

## 程式碼

```python
# LeetCode 179. Largest Number
# Time: O(n log n)  Space: O(n)

import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator: compare a+b vs b+a as strings
        strs = [str(num) for num in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        strs.sort(key=functools.cmp_to_key(compare))

        # Edge case: all zeros
        if strs[0] == '0':
            return '0'

        return ''.join(strs)
```

## 複雜度分析

- **時間複雜度:** O(n log n) for sorting
- **空間複雜度:** O(n) for the string representations
