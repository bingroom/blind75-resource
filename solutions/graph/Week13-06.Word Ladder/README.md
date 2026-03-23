# Word Ladder

- **LeetCode:** [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

## Problem Description

Given `beginWord`, `endWord`, and a `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, where each step changes exactly one letter and each intermediate word must be in `wordList`. Return 0 if no such sequence exists. The length counts both endpoints.


## Solution

```python
# LeetCode 127. Word Ladder
# Time: O(M^2 * N)  Space: O(M^2 * N)
# BFS with wildcard pattern buckets (M = word length, N = word list size)

from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Build adjacency via wildcard patterns: e.g. "hot" -> "*ot", "h*t", "ho*"
        L = len(beginWord)
        patterns = defaultdict(list)
        for word in word_set:
            for i in range(L):
                pattern = word[:i] + '*' + word[i + 1:]
                patterns[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()
            for i in range(L):
                pattern = word[:i] + '*' + word[i + 1:]
                for neighbor in patterns[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, steps + 1))
                # Clear bucket to avoid revisiting
                patterns[pattern] = []

        return 0
```

## Approach

BFS with wildcard pattern buckets:

1. Pre-process the word list: for each word, generate wildcard patterns by replacing each character with `*` (e.g., "hot" produces `*ot`, `h*t`, `ho*`). Map each pattern to its matching words.
2. BFS from `beginWord`. For each word, generate its patterns and look up neighbors via the pattern map.
3. Return the step count when `endWord` is found.
4. Clear each pattern bucket after use to avoid redundant work.

## Complexity

- **Time:** O(M^2 * N) where M is the word length and N is the word list size. Building patterns takes M^2 per word (substring operations), and BFS visits each word once.
- **Space:** O(M^2 * N) -- pattern map storage.
