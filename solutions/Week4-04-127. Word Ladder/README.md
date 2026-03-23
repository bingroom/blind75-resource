# Word Ladder

**Topic:** Graph
- **LeetCode 連結:** [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
- **難度:** Hard

## 題目描述

給定一個起始單字、一個目標單字和一組單字列表，每次只能變換一個字母，且變換後的單字必須在列表中。求從起始單字轉換到目標單字的最短轉換序列長度，若無法轉換則回傳 0。

## 解題思路

1. 將所有單字建立萬用字元模式的鄰接表（例如 "hot" 對應 "*ot"、"h*t"、"ho*"）。
2. 使用 BFS 從起始單字開始搜尋，每層代表一次轉換。
3. 對當前單字產生所有萬用字元模式，找出鄰居。
4. 若鄰居為目標單字，回傳當前步數 + 1。
5. 將未訪問的鄰居加入佇列，並標記為已訪問以避免重複。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(M^2 * N) where M is the word length and N is the word list size. Building patterns takes M^2 per word (substring operations), and BFS visits each word once.
- **空間複雜度:** O(M^2 * N) -- pattern map storage.
