# LeetCode 49. Group Anagrams
# 時間複雜度: O(n * k log k)  k 為最長字串長  空間複雜度: O(n * k)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        將 anagram 分在同一組。用「排序後字串」或「tuple 計數」當 key 分組。
        """
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
