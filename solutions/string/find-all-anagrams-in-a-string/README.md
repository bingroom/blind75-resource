# Find All Anagrams in a String

## Problem Description
Given two strings `s` and `p`, return a list of start indices of `p`'s anagrams in `s`. An anagram is a rearrangement of all characters.

## Approach
Sliding window of size `len(p)` over `s`. Maintain a frequency counter for the current window and compare it to the frequency counter of `p`. Slide the window by adding the new right character and removing the old left character.

## Complexity
- **Time:** O(n) where n = len(s)
- **Space:** O(1) -- at most 26 distinct characters in the counters
