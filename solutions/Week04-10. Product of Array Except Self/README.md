# Product of Array Except Self

**Topic:** Array

- **LeetCode:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

 

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `-30 <= nums[i] <= 30`

	- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

 

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## Solution

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

## 思路

- `output[i]` = (i 左邊所有數的乘積) × (i 右邊所有數的乘積)。
- 先從左到右掃一遍，在 `out[i]` 存「左乘積」；再從右到左掃一遍，乘上「右乘積」。兩遍即可，且只多用一個變數（left/right）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1) 額外（輸出不計）。

## 相關閱讀

- **演算法:** 前綴/後綴乘積 (prefix/suffix product)、兩遍掃描
