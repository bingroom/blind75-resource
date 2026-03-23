# Basic Calculator II

## Problem Description
Implement a basic calculator to evaluate a string expression containing non-negative integers and `+`, `-`, `*`, `/` operators (no parentheses). Integer division truncates toward zero.

## Approach
Track the previous operator and the current number. When a new operator is encountered (or end of string), apply the previous operator: for `+`/`-`, push the number (negated for `-`) onto the stack; for `*`/`/`, pop the top, compute the result, and push it back. This naturally handles operator precedence since `*` and `/` are resolved immediately while `+` and `-` defer to the final sum.

## Complexity
- **Time:** O(n)
- **Space:** O(n)
