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
