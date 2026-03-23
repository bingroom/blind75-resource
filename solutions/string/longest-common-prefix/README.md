# Longest Common Prefix

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.

## Approach
Vertical scanning: compare characters at the same position across all strings. Stop when a mismatch is found or any string is exhausted.

## Complexity
- **Time:** O(S) where S is the sum of all characters in all strings
- **Space:** O(1)
