# Top K Frequent Words

**Topic:** Heap
- **LeetCode 連結:** [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
- **難度:** Medium

## 題目描述

給定一組單字和一個整數 k，回傳出現頻率最高的前 k 個單字。若頻率相同，則按字典序排列。

## 解題思路

1. 使用 Counter 統計每個單字的出現次數。
2. 將每個單字以 (-頻率, 單字) 的格式放入列表。
3. 使用 heapq.nsmallest 取出前 k 個元素（負頻率確保高頻在前，字串比較確保字典序）。
4. 從結果中取出單字回傳。

## 程式碼

```python
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
```

## 複雜度分析

- **時間複雜度:** O(n log k)
- **空間複雜度:** O(n) for the counter
