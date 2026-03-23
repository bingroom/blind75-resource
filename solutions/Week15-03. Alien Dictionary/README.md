# Alien Dictionary

**Topic:** Graph

- **LeetCode:** [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

## Problem Description

Given a sorted list of words in an alien language, derive the order of characters in that language. Return the characters in sorted order. If the order is invalid, return an empty string. If multiple valid orderings exist, return any one.


## Solution

```python
# LeetCode 269. Alien Dictionary
# Time: O(C)  Space: O(1) -- O(U + min(U^2, N)) more precisely
# Topological sort (C = total chars across all words, U = unique chars)

from typing import List
from collections import deque, defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Collect all unique characters
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        # Compare adjacent words to derive ordering edges
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid case: prefix of w2 equals w1 but w1 is longer
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # Kahn's algorithm for topological sort
        q = deque(c for c in in_degree if in_degree[c] == 0)
        result = []

        while q:
            c = q.popleft()
            result.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # If not all chars are in result, there's a cycle
        if len(result) != len(in_degree):
            return ""

        return "".join(result)
```

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
