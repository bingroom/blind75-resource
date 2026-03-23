# Single Number

**Topic:** Binary
- **LeetCode 連結:** [136. Single Number](https://leetcode.com/problems/single-number/)
- **難度:** Easy

## 題目描述

給定一個非空整數陣列，除了某個元素只出現一次外，其餘每個元素都出現兩次。找出那個只出現一次的元素。

## 解題思路

1. 初始化結果為 0。
2. 對陣列中每個數字執行 XOR 運算。
3. 相同的數字 XOR 後互相抵消為 0，最終剩下的就是唯一的數字。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(1)
