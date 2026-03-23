# Word Break

**Topic:** Dynamic Programming

- **LeetCode:** [139. Word Break](https://leetcode.com/problems/word-break/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

 

**Example 1:**

```

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

```

**Example 2:**

```

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

```

**Example 3:**

```

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

```

 

**Constraints:**

	- `1 <= s.length <= 300`

	- `1 <= wordDict.length <= 1000`

	- `1 <= wordDict[i].length <= 20`

	- `s` and `wordDict[i]` consist of only lowercase English letters.

	- All the strings of `wordDict` are **unique**.

## Solution

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

## 思路

- **DP：** `dp[i]` 表示 s[:i] 可否被拆分。枚舉最後一個單詞的結尾 j，若 dp[j] 且 s[j:i] 在 wordDict 則 dp[i]=True。

## 時間 / 空間複雜度

- **時間:** O(n² · m)，m 為查詢單詞平均長度（set 查詢 O(m)）。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** Dynamic Programming、字串拆分
