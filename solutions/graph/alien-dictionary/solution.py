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
