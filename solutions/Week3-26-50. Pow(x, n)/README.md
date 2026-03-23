# Pow(x, n)

**Topic:** Math
- **LeetCode 連結:** [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
- **難度:** Medium

## 題目描述

實作 pow(x, n)，即計算 x 的 n 次方。n 為整數，可能為負數。

## 解題思路

1. 若 n 為負數，將 x 取倒數，n 取絕對值。
2. 使用快速冪法：若 n 為奇數，結果乘以 x。
3. 每次將 x 自乘，n 右移一位（除以 2）。
4. 直到 n 為 0，回傳結果。

## 程式碼

```python
# LeetCode 50. Pow(x, n)
# Time: O(log n)  Space: O(1)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n & 1:  # n is odd
                result *= x
            x *= x
            n >>= 1

        return result
```

## 複雜度分析

- **時間複雜度:** O(log n)
- **空間複雜度:** O(1)
