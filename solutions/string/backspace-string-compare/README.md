# Backspace String Compare

## Problem Description
Given two strings `s` and `t`, return true if they are equal when both are typed into empty text editors. `#` means a backspace character.

## Approach
Use two pointers starting from the end of each string. Track how many backspaces to apply (`skip` counter). When encountering `#`, increment skip; when skip > 0 on a regular character, decrement skip and move on. Compare the next valid characters from both strings.

## Complexity
- **Time:** O(m + n)
- **Space:** O(1)
