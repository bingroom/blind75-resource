# Evaluate Reverse Polish Notation

**Topic:** Stack

## Problem Description
Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix notation). Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division truncates toward zero.


## Solution

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

## Approach
Use a stack. Iterate through tokens: if the token is a number, push it onto the stack. If it is an operator, pop the top two elements, apply the operation (second-popped op first-popped), and push the result back. The final element on the stack is the answer. For division, use `int(a / b)` instead of `a // b` to ensure truncation toward zero (Python's floor division rounds toward negative infinity).

## Complexity
- **Time:** O(n)
- **Space:** O(n)
