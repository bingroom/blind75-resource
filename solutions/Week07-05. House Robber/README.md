# House Robber

**Topic:** Dynamic Programming

- **LeetCode:** [198. House Robber](https://leetcode.com/problems/house-robber/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

 

**Example 1:**

```

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

**Example 2:**

```

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 400`

## Solution

```python
# LeetCode 198. House Robber
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        相鄰不能同時偷，求最大金額。dp[i] = 考慮前 i 間的最大值，偷 i 則加 nums[i]+dp[i-2]，不偷則 dp[i-1]。
        """
        if not nums:
            return 0
        prev, cur = 0, nums[0]
        for i in range(1, len(nums)):
            prev, cur = cur, max(cur, prev + nums[i])
        return cur

```

## 思路

- **DP：** 到第 i 間的最大值 = max(偷 i：nums[i]+前 i-2 的最大, 不偷 i：前 i-1 的最大)。可壓成兩變數 prev, cur。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Dynamic Programming、線性 DP
