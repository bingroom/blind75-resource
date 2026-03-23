# Top K Frequent Words

## Problem Description
Given an array of strings `words` and an integer `k`, return the k most frequent strings. Sort the answer by frequency from highest to lowest, then alphabetically for ties.

## Approach
Count word frequencies with a Counter. Create tuples of `(-frequency, word)` so that sorting by these tuples naturally gives highest frequency first and lexicographic order for ties. Use `heapq.nsmallest(k)` to extract the top k.

## Complexity
- **Time:** O(n log k)
- **Space:** O(n) for the counter
