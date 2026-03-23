# Majority Element

**Topic:** Array
- **LeetCode 連結:** [169. Majority Element](https://leetcode.com/problems/majority-element/)
- **難度:** Easy

## 題目描述

給定一個大小為 n 的整數陣列，找出其中的多數元素。多數元素是指出現次數超過 n/2 的元素，保證該元素一定存在。

## 解題思路

1. 使用 Boyer-Moore 投票演算法，初始化候選人和計數器為 0。
2. 遍歷陣列，當計數為 0 時，將當前元素設為新的候選人。
3. 若當前元素等於候選人則計數加一，否則計數減一。
4. 遍歷結束後，候選人即為多數元素（因為多數元素出現次數超過一半，必定存活到最後）。

## 程式碼

```python
# LeetCode 169. Majority Element
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm.
        Maintain a candidate and a count. When count drops to 0,
        pick the current element as the new candidate. The majority
        element will always survive because it appears > n/2 times.
        """
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
```

## 複雜度分析

- **時間複雜度:** O(n) -- single pass through the array.
- **空間複雜度:** O(1) -- only two variables.
