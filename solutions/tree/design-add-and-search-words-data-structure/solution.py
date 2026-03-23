# LeetCode 211. Add and Search Word - Data structure design
# 時間複雜度: 插入 O(m) 查詢 O(m) 或 O(26^m) 含 '.'  空間複雜度: O(n*m)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def find(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == ".":
                return any(find(child, i + 1) for child in node.children.values())
            if c not in node.children:
                return False
            return find(node.children[c], i + 1)
        return find(self.root, 0)
