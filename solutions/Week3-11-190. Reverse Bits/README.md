# Reverse Bits

**Topic:** Binary
- **LeetCode 連結:** [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- **難度:** Easy

## 題目描述

給定一個 32 位無符號整數，將其二進位位元反轉後回傳結果。

## 解題思路

1. 初始化結果為 0。
2. 迴圈 32 次：將結果左移一位，取 n 的最低位元加到結果中。
3. 每次將 n 右移一位，處理下一個位元。

## 程式碼

```python
# LeetCode 190. Reverse Bits
# 時間複雜度: O(1) 32 次  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        將 32 位無符號整數的二進位反轉。從右到左取位，依序放到結果的左到右。
        """
        out = 0
        for _ in range(32):
            out = (out << 1) | (n & 1)
            n >>= 1
        return out
```

## 複雜度分析

- **時間複雜度:** O(1)（32 次）。
- **空間複雜度:** O(1)。
