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
