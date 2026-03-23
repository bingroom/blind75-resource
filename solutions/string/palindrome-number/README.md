# Palindrome Number

## Problem Description
Given an integer `x`, return true if `x` is a palindrome. Solve it without converting the integer to a string.

## Approach
Reverse only the second half of the number. Compare the first half with the reversed second half. For odd-length numbers, discard the middle digit from the reversed half by dividing by 10.

## Complexity
- **Time:** O(log n) -- we process half the digits
- **Space:** O(1)
