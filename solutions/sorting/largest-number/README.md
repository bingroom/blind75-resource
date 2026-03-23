# Largest Number

## Problem Description
Given a list of non-negative integers, arrange them such that they form the largest number and return it as a string.

## Approach
Convert numbers to strings and sort with a custom comparator: for two strings `a` and `b`, compare `a+b` vs `b+a`. The one that forms the larger concatenation should come first. Handle the edge case where all numbers are 0.

## Complexity
- **Time:** O(n log n) for sorting
- **Space:** O(n) for the string representations
