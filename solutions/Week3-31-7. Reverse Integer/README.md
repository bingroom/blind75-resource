# Reverse Integer

**Topic:** Math
- **LeetCode 連結:** [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- **難度:** Medium

## 題目描述

給定一個 32 位有號整數，將其數字反轉。若反轉後溢出 32 位整數範圍則回傳 0。

## 解題思路

1. 記錄正負號，對絕對值操作。
2. 每次取最後一位數字（模 10），加到反轉結果中。
3. 原數除以 10 去掉最後一位，重複直到為 0。
4. 檢查結果是否溢出 32 位整數範圍。

## 程式碼

```python
# LeetCode 7. Reverse Integer
# Time: O(log x)  Space: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0
        while x:
            digit = x % 10
            x //= 10
            result = result * 10 + digit

        result *= sign
        # Return 0 if overflow
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
```

## 複雜度分析

- **時間複雜度:** O(log x) -- number of digits
- **空間複雜度:** O(1)
