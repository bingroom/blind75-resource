# Longest Valid Parentheses

## Problem Description
Given a string containing just `(` and `)`, return the length of the longest valid (well-formed) parentheses substring.


## Solution

```python
# LeetCode 32. Longest Valid Parentheses
# Time: O(n)  Space: O(n)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack stores indices; bottom of stack is the boundary marker
        stack = [-1]  # initial boundary
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # No matching '(' -- push current index as new boundary
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
```

## Approach
Use a stack initialized with `-1` as a boundary marker. For each `(`, push its index. For each `)`, pop the stack: if the stack becomes empty, push the current index as a new boundary; otherwise, the current valid length is `i - stack[-1]`. Track the maximum.

## Complexity
- **Time:** O(n)
- **Space:** O(n)
