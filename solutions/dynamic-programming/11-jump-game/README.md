# Jump Game

- **LeetCode:** [55. Jump Game](https://leetcode.com/problems/jump-game/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true`* if you can reach the last index, or *`false`* otherwise*.

 

**Example 1:**

```

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

```

**Example 2:**

```

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `0 <= nums[i] <= 10^5`

## Solution

```python
# LeetCode 55. Jump Game
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        從索引 0 出發，nums[i] 為可跳最遠步數，能否到達最後一格。維護「最遠可達索引」即可。
        """
        reach = 0
        for i, x in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + x)
        return True

```

## 思路

- **貪心：** 維護「目前能到達的最遠索引」reach。若 i > reach 則無法到達；否則用 i + nums[i] 更新 reach。到最後即 True。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Greedy、Reachability
