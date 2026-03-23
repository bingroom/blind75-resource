# Ransom Note

- **LeetCode:** [383. Ransom Note](https://leetcode.com/problems/ransom-note/)

## Problem Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise. Each letter in `magazine` can only be used once in `ransomNote`.

## Approach

1. Count the frequency of every character in `magazine` using a hash map.
2. Iterate through `ransomNote`. For each character, check if the count in the map is positive.
3. If a character is missing or exhausted, return `False`. Otherwise decrement the count and continue.
4. If we finish the loop, every character was available — return `True`.

## Complexity

- **Time:** O(m + n) where m = len(ransomNote), n = len(magazine).
- **Space:** O(1) — the counter holds at most 26 lowercase English letters.
