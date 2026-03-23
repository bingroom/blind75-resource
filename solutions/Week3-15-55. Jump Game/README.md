# Jump Game

**Topic:** Dynamic Programming
- **LeetCode 連結:** [55. Jump Game](https://leetcode.com/problems/jump-game/)
- **難度:** Medium

## 題目描述

給定一個非負整數陣列，每個元素代表在該位置最多可跳躍的步數。判斷是否能從起點到達最後一個位置。

## 解題思路

1. 維護一個變數記錄目前能到達的最遠索引。
2. 遍歷陣列，若當前索引超過最遠可達位置，回傳 False。
3. 更新最遠可達位置為 max(reach, i + nums[i])。
4. 遍歷完成則回傳 True。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
