# Word Search II

**Topic:** Tree

- **LeetCode:** [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

```

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

```

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

```

 

**Constraints:**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 12`

	- `board[i][j]` is a lowercase English letter.

	- `1 <= words.length <= 3 * 10^4`

	- `1 <= words[i].length <= 10`

	- `words[i]` consists of lowercase English letters.

	- All the strings of `words` are unique.

## Solution

```python
# LeetCode 212. Word Search II
# 時間複雜度: O(m*n*4*3^(L-1)) + 建 Trie  空間複雜度: O(k*L) 單詞總長
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        在網格中找所有出現在 words 裡的單詞（相鄰格、每格最多用一次）。建 Trie，對每個格 DFS + 回溯，沿 Trie 走並在葉節點記錄單詞。
        """
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
        m, n = len(board), len(board[0])
        out = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            if node.word:
                out.append(node.word)
                node.word = None
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] not in node.children:
                return
            ch = board[r][c]
            board[r][c] = "#"
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(r + dr, c + dc, node.children[ch])
            board[r][c] = ch

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)
        return out

```

## 思路

- **Trie + DFS 回溯：** 先將 words 建成 Trie。對網格每個格子做 DFS，沿 Trie 走；若走到某節點有單詞則加入答案並清掉該節點單詞（去重）；用過格標記後還原。

## 時間 / 空間複雜度

- **時間:** 建 Trie O(總長) + 網格 DFS。
- **空間:** O(單詞總長度)。

## 相關閱讀

- **資料結構:** Trie
- **演算法:** DFS、Backtracking、Word Search I 進階
