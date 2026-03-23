# LeetCode 692. Top K Frequent Words
# Time: O(n log k)  Space: O(n)

import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        # Use a min-heap of size k. Negate frequency for max behavior.
        # For same frequency, we want lexicographically smaller, so
        # we use a wrapper to reverse string comparison.
        heap = []
        for word, freq in counts.items():
            # Negate freq so higher freq = smaller in heap
            # For tie-breaking, we need reverse lex order in a min-heap
            # so the lexicographically largest (least desired) gets popped first
            entry = (-freq, word)
            heap.append(entry)

        # Use nsmallest which is O(n log k)
        result = heapq.nsmallest(k, heap)
        return [word for _, word in result]
