# Basic Calculator II

## Problem Description
Implement a basic calculator to evaluate a string expression containing non-negative integers and `+`, `-`, `*`, `/` operators (no parentheses). Integer division truncates toward zero.


## Solution

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

## Approach
Track the previous operator and the current number. When a new operator is encountered (or end of string), apply the previous operator: for `+`/`-`, push the number (negated for `-`) onto the stack; for `*`/`/`, pop the top, compute the result, and push it back. This naturally handles operator precedence since `*` and `/` are resolved immediately while `+` and `-` defer to the final sum.

## Complexity
- **Time:** O(n)
- **Space:** O(n)
