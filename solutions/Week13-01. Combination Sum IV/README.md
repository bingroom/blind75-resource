# Combination Sum IV

**Topic:** Dynamic Programming

- **LeetCode:** [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an array of **distinct** integers `nums` and a target integer `target`, return *the number of possible combinations that add up to* `target`.

The test cases are generated so that the answer can fit in a **32-bit** integer.

 

**Example 1:**

```

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

```

**Example 2:**

```

Input: nums = [9], target = 3
Output: 0

```

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 1000`

	- All the elements of `nums` are **unique**.

	- `1 <= target <= 1000`

 

**Follow up:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

## Solution

```python
# LeetCode 377. Combination Sum IV (順序不同算不同)
# 時間複雜度: O(target * n)  空間複雜度: O(target)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        用 nums 中的數（可重複）湊出 target，順序不同算不同組合，求組合數。dp[i] = 湊出 i 的組合數。
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    dp[i] += dp[i - x]
        return dp[target]

```

## 思路

- **DP：** `dp[i]` = 湊出 i 的組合數。對每個 i 枚舉「最後一個用的數字」x，dp[i] += dp[i-x]。注意先枚舉 i 再枚舉 x 才能計入不同順序。

## 時間 / 空間複雜度

- **時間:** O(target × n)。
- **空間:** O(target)。

## 相關閱讀

- **演算法:** Dynamic Programming、計數型 DP
