# Number of 1 Bits

**Topic:** Binary
- **LeetCode 連結:** [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- **難度:** Easy

## 題目描述

給定一個無符號整數，計算其二進位表示中 1 的個數（漢明權重）。

## 解題思路

1. 初始化計數器為 0。
2. 每次執行 n &= n - 1，消除最右邊的一個 1 位元。
3. 每消除一次，計數器加 1，直到 n 為 0。

## 程式碼

```python
# LeetCode 191. Number of 1 Bits (Hamming weight)
# 時間複雜度: O(1) 位元數  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        計算 n 的二進位表示中 1 的個數。每次 n &= n - 1 會消掉最右邊一個 1。
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
```

## 複雜度分析

- **時間複雜度:** O(1)（位元數常數，例如 32）。
- **空間複雜度:** O(1)。
