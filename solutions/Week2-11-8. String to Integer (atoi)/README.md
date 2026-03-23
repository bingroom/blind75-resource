# String to Integer (atoi)

**Topic:** String
- **LeetCode 連結:** [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
- **難度:** Medium

## 題目描述

實作 atoi 函式，將字串轉換為 32 位元有號整數。需處理前導空白、可選的正負號、數字字元的讀取，以及溢位時裁切到 [-2^31, 2^31 - 1] 的範圍。

## 解題思路

1. 跳過字串前導的空白字元。
2. 檢查是否有正號或負號，記錄符號。
3. 逐一讀取數字字元，累積到結果中。
4. 每次累積前檢查是否會溢位，若溢位則回傳 INT_MAX 或 INT_MIN。
5. 回傳結果乘以符號。

## 程式碼

```python
# LeetCode 8. String to Integer (atoi)
# Time: O(n)  Space: O(1)


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
        i, n = 0, len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle optional sign
        sign = 1
        if i < n and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Read digits and convert
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(1)
