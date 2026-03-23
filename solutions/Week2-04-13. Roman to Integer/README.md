# Roman to Integer

**Topic:** Math
- **LeetCode 連結:** [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- **難度:** Easy

## 題目描述

給定一個羅馬數字字串，將其轉換為整數。羅馬數字包含 I、V、X、L、C、D、M 七個字元，特殊規則如 IV=4、IX=9 等需以減法處理。

## 解題思路

1. 建立羅馬字元到數值的對應表。
2. 從左到右遍歷字串中的每個字元。
3. 若當前字元的值小於下一個字元的值，則減去當前值（如 IV 中的 I）。
4. 否則加上當前值，最終累加結果即為整數。

## 程式碼

```python
# LeetCode 13. Roman to Integer
# Time: O(n)  Space: O(1)


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            # If current value < next value, subtract (e.g., IV = 4)
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]
        return result
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(1)
