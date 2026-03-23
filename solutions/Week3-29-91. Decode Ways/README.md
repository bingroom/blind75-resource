# Decode Ways

**Topic:** Dynamic Programming
- **LeetCode 連結:** [91. Decode Ways](https://leetcode.com/problems/decode-ways/)
- **難度:** Medium

## 題目描述

給定一個數字字串，每個數字或兩位數字可對應一個字母（A=1, B=2, ..., Z=26）。計算共有多少種解碼方式。

## 解題思路

1. 使用動態規劃，dp[i] 表示前 i 個字元的解碼方式數。
2. 若當前字元不為 '0'，可單獨解碼：dp[i] += dp[i-1]。
3. 若前兩個字元組成的數字在 10-26 之間，可雙字元解碼：dp[i] += dp[i-2]。
4. 用兩個變數滾動優化空間。

## 程式碼

```python
# LeetCode 91. Decode Ways
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        數字串可解碼成 A=1..Z=26，求解碼方法數。dp[i] 與 dp[i-1]、dp[i-2] 有關（單字元 / 雙字元）。
        """
        if not s or s[0] == "0":
            return 0
        prev, cur = 1, 1
        for i in range(1, len(s)):
            next_ = 0
            if s[i] != "0":
                next_ += cur
            two = int(s[i - 1 : i + 1])
            if 10 <= two <= 26:
                next_ += prev
            prev, cur = cur, next_
        return cur
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
