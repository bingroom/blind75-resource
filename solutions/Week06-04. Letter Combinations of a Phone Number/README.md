# Letter Combinations of a Phone Number

**Topic:** Backtracking

- **LeetCode:** [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent (like on a phone keypad).


## Solution

```python
# LeetCode 17. Letter Combinations of a Phone Number
# Time: O(4^n)  Space: O(n) recursion depth

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []

        def backtrack(idx: int, path: List[str]):
            if idx == len(digits):
                result.append(''.join(path))
                return
            for ch in phone[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return result
```

## Approach

Backtracking over each digit position.

1. Map each digit to its corresponding letters (e.g., '2' -> "abc").
2. For digit at index `idx`, iterate over all mapped letters.
3. Append the letter, recurse to the next index, then backtrack.
4. When `idx` equals the length of digits, join the path and add to results.

## Complexity

- **Time:** O(4^n) where n is the length of digits (worst case: digits like '7' and '9' map to 4 letters)
- **Space:** O(n) for the recursion depth
