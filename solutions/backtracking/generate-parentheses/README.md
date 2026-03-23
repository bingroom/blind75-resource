# Generate Parentheses

- **LeetCode:** [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

## Problem Description

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Approach

Backtracking with two counters: `open_count` and `close_count`.

1. We can add `(` if `open_count < n`.
2. We can add `)` only if `close_count < open_count` (ensures validity).
3. When the path length reaches `2 * n`, we have a complete valid combination.
4. These two constraints naturally prune the search space to only valid strings.

## Complexity

- **Time:** O(4^n / sqrt(n)) -- the nth Catalan number bounds the number of valid combinations
- **Space:** O(n) for the recursion depth
