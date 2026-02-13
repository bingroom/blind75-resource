# Word Break

- **LeetCode:** [139. Word Break](https://leetcode.com/problems/word-break/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

判斷字串 s 是否可由 wordDict 中的單詞（可重複）拼接而成。

## 思路

- **DP：** `dp[i]` 表示 s[:i] 可否被拆分。枚舉最後一個單詞的結尾 j，若 dp[j] 且 s[j:i] 在 wordDict 則 dp[i]=True。

## 時間 / 空間複雜度

- **時間:** O(n² · m)，m 為查詢單詞平均長度（set 查詢 O(m)）。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** Dynamic Programming、字串拆分
