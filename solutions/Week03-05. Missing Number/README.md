# Missing Number

**Topic:** Bit Manipulation

- **LeetCode:** [268. Missing Number](https://leetcode.com/problems/missing-number/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

 

**Example 1:**

**Input:** nums = [3,0,1]

**Output:** 2

**Explanation:**

`n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 2:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

`n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 3:**

**Input:** nums = [9,6,4,2,3,5,7,0,1]

**Output:** 8

**Explanation:**

`n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

 

 

 

 

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 10^4`

	- `0 <= nums[i] <= n`

	- All the numbers of `nums` are **unique**.

 

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## Solution

```python
# LeetCode 268. Missing Number
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        陣列含 n 個數，取值為 [0, n] 且不重複，找缺的那一個。
        法一：預期和 0+1+..+n = n*(n+1)//2，減去實際和即缺的數。
        """
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)

```

## 思路

- **數學：** 預期和 = 0+1+...+n = n(n+1)/2，減去陣列實際和即為缺的數。
- **位元：** 用 XOR，把 0..n 與所有 nums 做 XOR，最後剩下缺的數。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Math、XOR 性質（可選）
