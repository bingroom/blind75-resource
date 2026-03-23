# House Robber II

- **LeetCode:** [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

 

**Example 1:**

```

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

```

**Example 2:**

```

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

**Example 3:**

```

Input: nums = [1,2,3]
Output: 3

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 1000`

## Solution

```python
# LeetCode 213. House Robber II (環狀)
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        房子排成環，相鄰不能偷。拆成兩段線性：不偷第一間、不偷最後一間，取兩次 House Robber I 的較大值。
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_range(arr: List[int]) -> int:
            prev, cur = 0, arr[0]
            for i in range(1, len(arr)):
                prev, cur = cur, max(cur, prev + arr[i])
            return cur

        return max(rob_range(nums[:-1]), rob_range(nums[1:]))

```

## 思路

- 環狀可拆成兩種線性：**不偷第一間**（考慮 nums[1:]）、**不偷最後一間**（考慮 nums[:-1]）。分別做 House Robber I，取較大值。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** DP、環狀拆成線性
