# Backspace String Compare

**Topic:** Stack
- **LeetCode 連結:** [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
- **難度:** Easy

## 題目描述

給定兩個字串 s 和 t，其中 '#' 代表退格鍵。判斷兩個字串在經過退格處理後是否相等。要求使用 O(1) 額外空間。

## 解題思路

1. 使用雙指標從兩個字串的末尾向前遍歷。
2. 遇到 '#' 時計算需要跳過的字元數，遇到普通字元且有跳過計數時則跳過。
3. 找到兩個字串各自的下一個有效字元後進行比較。
4. 若兩個有效字元不同，或一個字串已結束而另一個還有有效字元，則回傳 false。

## 程式碼

```python
# LeetCode 844. Backspace String Compare
# Time: O(m + n)  Space: O(1)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Two-pointer approach from the end to achieve O(1) space
        i, j = len(s) - 1, len(t) - 1
        skip_s = skip_t = 0

        while i >= 0 or j >= 0:
            # Find next valid char in s
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            # Find next valid char in t
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # Compare characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False  # one string is exhausted but the other isn't

            i -= 1
            j -= 1

        return True
```

## 複雜度分析

- **時間複雜度:** O(m + n)
- **空間複雜度:** O(1)
