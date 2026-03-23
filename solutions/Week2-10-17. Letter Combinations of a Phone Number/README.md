# Letter Combinations of a Phone Number

**Topic:** Recursion
- **LeetCode 連結:** [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- **難度:** Medium

## 題目描述

給定一個僅包含數字 2-9 的字串，回傳該數字在電話按鍵上所能代表的所有字母組合。數字與字母的對應關係和電話按鍵相同。

## 解題思路

1. 建立數字到字母的對應表（如 '2' -> "abc"）。
2. 使用回溯法，從第一個數字開始逐一嘗試對應的每個字母。
3. 將當前字母加入路徑，遞迴處理下一個數字。
4. 當路徑長度等於輸入長度時，將組合加入結果。
5. 回溯：移除最後加入的字母，嘗試下一個選擇。

## 程式碼

```python
# LeetCode 17. Letter Combinations of a Phone Number
# Time: O(4^n)  Space: O(n) recursion depth

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []

        def backtrack(idx: int, path: List[str]):
            if idx == len(digits):
                result.append(''.join(path))
                return
            for ch in phone[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return result
```

## 複雜度分析

- **時間複雜度:** O(4^n) where n is the length of digits (worst case: digits like '7' and '9' map to 4 letters)
- **空間複雜度:** O(n) for the recursion depth
