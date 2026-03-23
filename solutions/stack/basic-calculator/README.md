# Basic Calculator

## Problem Description
Implement a basic calculator to evaluate a string expression containing `+`, `-`, `(`, `)`, non-negative integers, and spaces.

## Approach
Maintain a running `result`, a `sign` (+1 or -1), and a stack for handling parentheses. For digits, build the current number. For `+`/`-`, add the completed number to the result and update the sign. On `(`, push the current result and sign onto the stack and reset. On `)`, finalize the inner expression, pop the saved sign and result, and combine: `result = prev_result + prev_sign * result`. After the loop, add any trailing number.

## Complexity
- **Time:** O(n)
- **Space:** O(n) for the stack in the worst case with nested parentheses
