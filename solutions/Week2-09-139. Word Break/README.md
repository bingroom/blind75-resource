# Word Break

**Topic:** Trie
- **LeetCode 連結:** [139. Word Break](https://leetcode.com/problems/word-break/)
- **難度:** Medium

## 題目描述

給定一個字串 s 和一個單詞字典 wordDict，判斷 s 是否可以被拆分為一個或多個字典中的單詞。字典中的單詞可以重複使用。

## 解題思路

1. 建立布林陣列 dp，dp[i] 表示 s[:i] 是否可被拆分，初始 dp[0] = True。
2. 將 wordDict 轉為集合以加速查詢。
3. 對每個位置 i，遍歷所有可能的切割點 j，若 dp[j] 為 True 且 s[j:i] 在字典中，則 dp[i] = True。
4. 回傳 dp[n] 即為最終答案。

## 程式碼

```python
# LeetCode 139. Word Break
# 時間複雜度: O(n² * m)  n=len(s), m=平均單詞長  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        判斷 s 是否可由 wordDict 中的單詞（可重複使用）拼接而成。dp[i] = s[:i] 可否被拆分。
        """
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]
```

## 複雜度分析

- **時間複雜度:** O(n² · m)，m 為查詢單詞平均長度（set 查詢 O(m)）。
- **空間複雜度:** O(n)。
