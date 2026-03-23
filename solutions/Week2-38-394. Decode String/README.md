# Decode String

**Topic:** Stack
- **LeetCode 連結:** [394. Decode String](https://leetcode.com/problems/decode-string/)
- **難度:** Medium

## 題目描述

給定一個經過編碼的字串，規則為 k[encoded_string]，表示方括號內的字串重複 k 次。回傳解碼後的字串。編碼可以巢狀。

## 解題思路

1. 使用堆疊儲存外層的字串和重複次數。
2. 遇到數字時累加組成完整的重複次數。
3. 遇到 '[' 時將當前字串和重複次數壓入堆疊，重置狀態。
4. 遇到 ']' 時從堆疊彈出外層狀態，將當前字串重複指定次數後接在外層字串之後。
5. 遇到字母時直接加到當前字串。

## 程式碼

```python
# LC 394. Decode String (Medium)
# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                # Save current state and start fresh
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif ch == ']':
                # Pop previous state and repeat current string
                prev_str, repeat = stack.pop()
                cur_str = prev_str + cur_str * repeat
            else:
                cur_str += ch

        return cur_str
```

## 複雜度分析

- **時間複雜度:** O(n * max_k) where n is the length of the output string and max_k is the maximum nesting multiplier
- **空間複雜度:** O(n) for the stack and output string
