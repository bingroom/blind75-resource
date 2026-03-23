# Basic Calculator II

**Topic:** Stack
- **LeetCode 連結:** [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
- **難度:** Medium

## 題目描述

實作一個基本計算器，計算包含加減乘除和空白的字串表達式的值。整數除法向零取整。

## 解題思路

1. 使用堆疊處理運算子優先順序。
2. 遍歷字串，遇到數字時累計當前數值。
3. 遇到運算子或到達字串尾端時，根據前一個運算子決定操作：加減直接推入堆疊，乘除與堆疊頂端運算後推入。
4. 最終堆疊中所有數字的總和即為結果。

## 程式碼

```python
# LC 227. Basic Calculator II (Medium)
# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_num = 0
        op = '+'  # previous operator

        for i, ch in enumerate(s):
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)

            # Process when we hit an operator or end of string
            if ch in "+-*/" or i == len(s) - 1:
                if op == '+':
                    stack.append(cur_num)
                elif op == '-':
                    stack.append(-cur_num)
                elif op == '*':
                    stack.append(stack.pop() * cur_num)
                elif op == '/':
                    stack.append(int(stack.pop() / cur_num))
                op = ch
                cur_num = 0

        return sum(stack)
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(n)
