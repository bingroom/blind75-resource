# Longest Valid Parentheses

## Problem Description
Given a string containing just `(` and `)`, return the length of the longest valid (well-formed) parentheses substring.

## Approach
Use a stack initialized with `-1` as a boundary marker. For each `(`, push its index. For each `)`, pop the stack: if the stack becomes empty, push the current index as a new boundary; otherwise, the current valid length is `i - stack[-1]`. Track the maximum.

## Complexity
- **Time:** O(n)
- **Space:** O(n)
