# Basic Calculator

**Topic:** Stack
- **LeetCode 連結:** [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)
- **難度:** Hard

## 題目描述

實作一個基本計算機，計算包含 `+`、`-`、`(` 和 `)` 的字串運算式的值。字串中可能包含空格，數字為非負整數。

## 解題思路

1. 維護一個結果變數、當前數字和正負號。
2. 遇到數字時累加組成完整數值。
3. 遇到 `+` 或 `-` 時將先前的數字加入結果，並更新正負號。
4. 遇到 `(` 時將目前結果和正負號壓入堆疊，重置結果。
5. 遇到 `)` 時將括號內的結果與堆疊中的外層結果合併。
6. 最後加上尚未處理的最後一個數字。

## 程式碼

```python
# LC 224. Basic Calculator (Hard)
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1  # +1 or -1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                # Save current result and sign, then reset
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                # Finalize the expression inside parentheses
                result += sign * num
                num = 0
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result

        # Don't forget the last number
        result += sign * num
        return result
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(n) for the stack in the worst case with nested parentheses
