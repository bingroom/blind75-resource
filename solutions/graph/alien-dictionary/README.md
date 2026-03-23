# Alien Dictionary

- **LeetCode:** [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

## Problem Description

Given a sorted list of words in an alien language, derive the order of characters in that language. Return the characters in sorted order. If the order is invalid, return an empty string. If multiple valid orderings exist, return any one.

## Approach

Topological sort:

1. Collect all unique characters from the word list.
2. Compare each pair of adjacent words to find the first differing character -- this gives a directed edge (ordering constraint).
3. Detect the invalid case where a longer word appears before its prefix.
4. Run Kahn's algorithm (BFS topological sort) using the derived edges and in-degree counts.
5. If the result contains all unique characters, return it; otherwise a cycle exists, so return an empty string.

## Complexity

- **Time:** O(C) where C is the total number of characters across all words.
- **Space:** O(U) where U is the number of unique characters (at most 26).
