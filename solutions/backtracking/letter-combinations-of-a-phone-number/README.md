# Letter Combinations of a Phone Number

- **LeetCode:** [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent (like on a phone keypad).

## Approach

Backtracking over each digit position.

1. Map each digit to its corresponding letters (e.g., '2' -> "abc").
2. For digit at index `idx`, iterate over all mapped letters.
3. Append the letter, recurse to the next index, then backtrack.
4. When `idx` equals the length of digits, join the path and add to results.

## Complexity

- **Time:** O(4^n) where n is the length of digits (worst case: digits like '7' and '9' map to 4 letters)
- **Space:** O(n) for the recursion depth
