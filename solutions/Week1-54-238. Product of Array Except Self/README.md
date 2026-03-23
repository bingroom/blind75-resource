# Product of Array Except Self

**Topic:** Array
- **LeetCode 連結:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- **難度:** Medium

## 題目描述

給定一個整數陣列 `nums`，回傳一個陣列 `output`，其中 `output[i]` 等於 `nums` 中除了 `nums[i]` 以外所有元素的乘積。要求不使用除法，且在 O(n) 時間內完成。

## 解題思路

1. 第一次從左到右遍歷，計算每個位置左邊所有元素的乘積，存入結果陣列。
2. 第二次從右到左遍歷，維護一個「右邊乘積」變數。
3. 將結果陣列中每個位置乘上「右邊乘積」，即得到除自身以外的完整乘積。
4. 每步更新「右邊乘積」，最終回傳結果陣列。

## 程式碼

```python
# LeetCode 238. Product of Array Except Self
# 時間複雜度: O(n)  空間複雜度: O(1) 不含輸出陣列
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        回傳 output[i] = 除 nums[i] 外所有數的乘積。限制：不能用除法、盡量 O(1) 額外空間。
        做法：output[i] = (i 左邊所有數的乘積) * (i 右邊所有數的乘積)。
        先從左掃一遍填「左乘積」，再從右掃一遍乘上「右乘積」。
        """
        n = len(nums)
        out = [1] * n
        # 第一遍：out[i] = nums[0]*...*nums[i-1]（i 左邊的乘積）
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]
        # 第二遍：從右往左，乘上「右邊的乘積」
        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]
        return out
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1) 額外（輸出不計）。
