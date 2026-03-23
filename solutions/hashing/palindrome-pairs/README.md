# Palindrome Pairs

- **LeetCode:** [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

## Problem Description

Given a list of unique words, return all pairs of distinct indices `(i, j)` such that the concatenation `words[i] + words[j]` is a palindrome.

## Approach

1. Build a hash map from each word to its index for O(1) lookups.
2. For each word, consider every split point `j` from 0 to len(word), producing a prefix `word[:j]` and suffix `word[j:]`.
3. **Case 1 — prefix is a palindrome:** If the reverse of the suffix exists in the map (and is a different word), then placing that reversed suffix before the current word yields a palindrome: `rev(suffix) + prefix + suffix` where `prefix` is already a palindrome.
4. **Case 2 — suffix is a palindrome:** If the reverse of the prefix exists in the map, then placing it after the current word yields a palindrome: `prefix + suffix + rev(prefix)`.
5. The `suffix` non-empty check in Case 2 prevents counting the same pair twice (the `j == n` split in Case 1 already handles the full-word-reverse scenario).

## Complexity

- **Time:** O(n * k^2) where n is the number of words and k is the maximum word length. For each word we check k+1 splits, and each palindrome check / string reversal costs O(k).
- **Space:** O(n * k) for the hash map storing all words.
