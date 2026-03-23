# Counting Bits

**Topic:** Binary
- **LeetCode 連結:** [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
- **難度:** Easy

## 題目描述

給定一個非負整數 n，對於 0 到 n 的每個數，計算其二進位表示中 1 的個數，以陣列形式回傳。

## 解題思路

1. 建立 dp 陣列，dp[0] = 0。
2. 利用位元運算的遞推關係：dp[i] = dp[i >> 1] + (i & 1)。
3. i >> 1 是 i 去掉最低位的數，i & 1 判斷最低位是否為 1。
4. 從 1 到 n 逐一計算即可。

## 程式碼

```python
# LeetCode 338. Counting Bits
# 時間複雜度: O(n)  空間複雜度: O(1) 不含輸出
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        對 0..n 每個數回傳其二進位中 1 的個數。DP：i 的 1 的個數 = i>>1 的個數 + (i&1)。
        """
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1) 額外（不含輸出陣列）。
