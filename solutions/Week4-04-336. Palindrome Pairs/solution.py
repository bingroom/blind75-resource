# LeetCode 336. Palindrome Pairs
# Time: O(n * k^2)  Space: O(n * k)
# where n = number of words, k = max word length


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        """
        For each word, check all possible splits into prefix and suffix.
        If the prefix is a palindrome and the reverse of the suffix exists
        in the map, then (reverse_suffix_index, current_index) forms a pair.
        Symmetrically for suffix being a palindrome.
        """
        word_map = {w: i for i, w in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: prefix is palindrome
                # Then rev(suffix) + prefix + suffix is a palindrome
                # So we need rev(suffix) in the map, placed before word
                if prefix == prefix[::-1]:
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_map and word_map[rev_suffix] != i:
                        result.append([word_map[rev_suffix], i])

                # Case 2: suffix is palindrome (and suffix is non-empty to avoid duplicates)
                # Then prefix + suffix + rev(prefix) is a palindrome
                # So we need rev(prefix) in the map, placed after word
                if suffix and suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_map and word_map[rev_prefix] != i:
                        result.append([i, word_map[rev_prefix]])

        return result
