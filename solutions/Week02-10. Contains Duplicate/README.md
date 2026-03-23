# Contains Duplicate

**Topic:** Hashing

- **LeetCode:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

 

**Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## Solution

```python
# LeetCode 217. Contains Duplicate
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        判斷陣列中是否有重複元素。
        用 set 記錄已見過的數，遇過就回傳 True。
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False

```

## 思路

- 用 **set** 存已見過的數，遍歷時若 `x in seen` 則回傳 `True`，否則 `seen.add(x)`。遍歷完回傳 `False`。
- 另解：排序後相鄰比較，時間 O(n log n)，空間 O(1)（若可改原陣列）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Set（集合）、Hash Table
