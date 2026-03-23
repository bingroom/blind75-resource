# Word Ladder

- **LeetCode:** [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

## Problem Description

Given `beginWord`, `endWord`, and a `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, where each step changes exactly one letter and each intermediate word must be in `wordList`. Return 0 if no such sequence exists. The length counts both endpoints.

## Approach

BFS with wildcard pattern buckets:

1. Pre-process the word list: for each word, generate wildcard patterns by replacing each character with `*` (e.g., "hot" produces `*ot`, `h*t`, `ho*`). Map each pattern to its matching words.
2. BFS from `beginWord`. For each word, generate its patterns and look up neighbors via the pattern map.
3. Return the step count when `endWord` is found.
4. Clear each pattern bucket after use to avoid redundant work.

## Complexity

- **Time:** O(M^2 * N) where M is the word length and N is the word list size. Building patterns takes M^2 per word (substring operations), and BFS visits each word once.
- **Space:** O(M^2 * N) -- pattern map storage.
