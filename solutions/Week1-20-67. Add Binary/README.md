# Add Binary

**Topic:** Binary
- **LeetCode 連結:** [67. Add Binary](https://leetcode.com/problems/add-binary/)
- **難度:** Easy

## 題目描述

給定兩個二進位字串 a 和 b，回傳它們的二進位相加結果（也是字串形式）。

## 解題思路

1. 從兩個字串的末尾開始，逐位相加並維護進位。
2. 每一位的總和為兩個數字加上進位，結果的該位為 total % 2，新的進位為 total // 2。
3. 將每一位的結果存入陣列，處理完所有位數和進位後反轉陣列。
4. 將結果陣列合併為字串回傳。

## 程式碼

```python
# LeetCode 67. Add Binary
# Time: O(max(m, n))  Space: O(max(m, n))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))
```

## 複雜度分析

- **時間複雜度:** O(max(m, n))
- **空間複雜度:** O(max(m, n)) for the result
