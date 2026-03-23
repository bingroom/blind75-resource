# Evaluate Reverse Polish Notation

## Problem Description
Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix notation). Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division truncates toward zero.

## Approach
Use a stack. Iterate through tokens: if the token is a number, push it onto the stack. If it is an operator, pop the top two elements, apply the operation (second-popped op first-popped), and push the result back. The final element on the stack is the answer. For division, use `int(a / b)` instead of `a // b` to ensure truncation toward zero (Python's floor division rounds toward negative infinity).

## Complexity
- **Time:** O(n)
- **Space:** O(n)
