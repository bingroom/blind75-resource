# Evaluate Reverse Polish Notation

**Topic:** Stack
- **LeetCode 連結:** [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- **難度:** Medium

## 題目描述

給定一個字串陣列 `tokens`，代表逆波蘭表示法（後序表示法）的算術運算式，計算並回傳其運算結果。有效的運算子為 `+`、`-`、`*`、`/`，除法向零取整。

## 解題思路

1. 使用堆疊來處理運算式。
2. 遍歷每個 token：若為數字則推入堆疊。
3. 若為運算子，從堆疊彈出兩個運算元（注意順序：先彈出的是右運算元），執行對應運算後將結果推回堆疊。
4. 遍歷結束後，堆疊中剩餘的唯一元素即為最終結果。

## 程式碼

```python
# LC 150. Evaluate Reverse Polish Notation (Medium)
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/" and len(token) == 1:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    # Truncate toward zero (Python's // floors, so use int())
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(n)
