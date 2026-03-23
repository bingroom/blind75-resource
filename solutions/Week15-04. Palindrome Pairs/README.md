# Palindrome Pairs

**Topic:** Hashing

- **LeetCode:** [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)

## Problem Description

Given a list of unique words, return all pairs of distinct indices `(i, j)` such that the concatenation `words[i] + words[j]` is a palindrome.


## Solution

```python
# LeetCode 336. Palindrome Pairs
# Time: O(n * k^2)  Space: O(n * k)
# where n = number of words, k = max word length


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        """
        For each word, check all possible splits into prefix and suffix.
        If the prefix is a palindrome and the reverse of the suffix exists
        in the map, then (reverse_suffix_index, current_index) forms a pair.
        Symmetrically for suffix being a palindrome.
        """
        word_map = {w: i for i, w in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: prefix is palindrome
                # Then rev(suffix) + prefix + suffix is a palindrome
                # So we need rev(suffix) in the map, placed before word
                if prefix == prefix[::-1]:
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_map and word_map[rev_suffix] != i:
                        result.append([word_map[rev_suffix], i])

                # Case 2: suffix is palindrome (and suffix is non-empty to avoid duplicates)
                # Then prefix + suffix + rev(prefix) is a palindrome
                # So we need rev(prefix) in the map, placed after word
                if suffix and suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_map and word_map[rev_prefix] != i:
                        result.append([i, word_map[rev_prefix]])

        return result
```

## Approach

1. Build a hash map from each word to its index for O(1) lookups.
2. For each word, consider every split point `j` from 0 to len(word), producing a prefix `word[:j]` and suffix `word[j:]`.
3. **Case 1 — prefix is a palindrome:** If the reverse of the suffix exists in the map (and is a different word), then placing that reversed suffix before the current word yields a palindrome: `rev(suffix) + prefix + suffix` where `prefix` is already a palindrome.
4. **Case 2 — suffix is a palindrome:** If the reverse of the prefix exists in the map, then placing it after the current word yields a palindrome: `prefix + suffix + rev(prefix)`.
5. The `suffix` non-empty check in Case 2 prevents counting the same pair twice (the `j == n` split in Case 1 already handles the full-word-reverse scenario).

## Complexity

- **Time:** O(n * k^2) where n is the number of words and k is the maximum word length. For each word we check k+1 splits, and each palindrome check / string reversal costs O(k).
- **Space:** O(n * k) for the hash map storing all words.
