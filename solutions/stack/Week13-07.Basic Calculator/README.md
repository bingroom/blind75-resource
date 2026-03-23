# Basic Calculator

## Problem Description
Implement a basic calculator to evaluate a string expression containing `+`, `-`, `(`, `)`, non-negative integers, and spaces.


## Solution

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

## Approach
Maintain a running `result`, a `sign` (+1 or -1), and a stack for handling parentheses. For digits, build the current number. For `+`/`-`, add the completed number to the result and update the sign. On `(`, push the current result and sign onto the stack and reset. On `)`, finalize the inner expression, pop the saved sign and result, and combine: `result = prev_result + prev_sign * result`. After the loop, add any trailing number.

## Complexity
- **Time:** O(n)
- **Space:** O(n) for the stack in the worst case with nested parentheses
