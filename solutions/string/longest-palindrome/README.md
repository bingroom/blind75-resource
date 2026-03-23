# Longest Palindrome

## Problem Description
Given a string `s` of lowercase and uppercase letters, return the length of the longest palindrome that can be built with those letters.

## Approach
Count character frequencies. Every pair of identical characters contributes 2 to the palindrome length. At most one character with an odd count can be placed in the center, adding 1.

## Complexity
- **Time:** O(n)
- **Space:** O(1) -- bounded by alphabet size
