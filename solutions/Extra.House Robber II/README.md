# House Robber II

**Topic:** Unknown
- **LeetCode 連結:** [0. House Robber II](https://leetcode.com/problems/house-robber-ii/)
- **難度:** Medium

## 題目描述

房屋排列成環形，相鄰房屋不能同時偷竊。給定每間房屋的金額，計算在不觸發警報的情況下能偷到的最大金額。

## 解題思路

1. 環形結構意味著第一間和最後一間不能同時偷。
2. 拆成兩個線性子問題：不偷第一間（nums[1:]）和不偷最後一間（nums[:-1]）。
3. 對每個子問題用 House Robber I 的動態規劃求解。
4. 取兩者的較大值為答案。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
