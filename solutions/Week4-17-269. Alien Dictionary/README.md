# Alien Dictionary

**Topic:** Graph
- **LeetCode 連結:** [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- **難度:** Hard

## 題目描述

給定一組按外星語言字典序排列的單詞，推導出該語言的字母順序。若順序無效則回傳空字串。

## 解題思路

1. 比較相鄰單詞的第一個不同字元，建立有向圖和入度表。
2. 檢查無效情況（前綴相同但前者較長）。
3. 使用拓撲排序（Kahn 演算法）：從入度為 0 的節點開始 BFS。
4. 若排序結果包含所有字元則有效，否則存在環，回傳空字串。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(C) where C is the total number of characters across all words.
- **空間複雜度:** O(U) where U is the number of unique characters (at most 26).
