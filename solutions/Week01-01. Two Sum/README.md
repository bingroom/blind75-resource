# Two Sum

**Topic:** Array

- **LeetCode:** [1. Two Sum](https://leetcode.com/problems/two-sum/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

 

**Example 1:**

```

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

```

**Example 2:**

```

Input: nums = [3,2,4], target = 6
Output: [1,2]

```

**Example 3:**

```

Input: nums = [3,3], target = 6
Output: [0,1]

```

 

**Constraints:**

	- `2 <= nums.length <= 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- `-10^9 <= target <= 10^9`

	- **Only one valid answer exists.**

 
**Follow-up: **Can you come up with an algorithm that is less than `O(n^2)` time complexity?

## Solution

```python
# LeetCode 1. Two Sum
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        在陣列中找兩數之和等於 target，回傳兩數的索引。
        使用 Hash Map 一次遍歷：邊走邊查「target - 當前值」是否已出現。
        """
        # seen[數值] = 索引，用來 O(1) 查詢「互補數」是否出現過
        seen = {}
        for i, x in enumerate(nums):
            # 互補數 = target - 當前數，若在 seen 裡表示之前已出現過
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []

```

## 思路

- 暴力：雙迴圈枚舉 (i, j)，時間 O(n²)。
- 優化：用 **Hash Map** 存「已見過的數 → 索引」。遍歷時檢查 `target - nums[i]` 是否在 map 裡，有則回傳 `[map[need], i]`。

## 時間 / 空間複雜度

- **時間:** O(n)，單次遍歷 + 查表 O(1)。
- **空間:** O(n)，最壞存 n 個數。

## 相關閱讀

- **資料結構:** Hash Table（雜湊表）
- **演算法:** 以空間換時間、一次遍歷 (one-pass)
