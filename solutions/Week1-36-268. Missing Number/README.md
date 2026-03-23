# Missing Number

**Topic:** Binary
- **LeetCode 連結:** [268. Missing Number](https://leetcode.com/problems/missing-number/)
- **難度:** Easy

## 題目描述

給定一個包含 n 個不重複數字的陣列，取值範圍為 [0, n]，找出缺少的那個數字。

## 解題思路

1. 計算 0 到 n 的預期總和：n * (n + 1) / 2。
2. 計算陣列的實際總和。
3. 兩者之差即為缺少的數字。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
