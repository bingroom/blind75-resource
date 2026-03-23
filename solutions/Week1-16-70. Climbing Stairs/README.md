# Climbing Stairs

**Topic:** Dynamic Programming
- **LeetCode 連結:** [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- **難度:** Easy

## 題目描述

你正在爬一個有 `n` 階的樓梯，每次可以爬 1 階或 2 階。求有多少種不同的方式可以爬到頂端。

## 解題思路

1. 此題本質為費波那契數列：到第 `i` 階的方法數等於到第 `i-1` 階加上第 `i-2` 階的方法數。
2. 基礎情況：`n=1` 時有 1 種，`n=2` 時有 2 種。
3. 使用兩個變數 `a` 和 `b` 滾動計算，避免使用完整的 DP 陣列。
4. 從第 3 階迭代到第 `n` 階，每步令 `a, b = b, a + b`，最終 `b` 即為答案。

## 程式碼

```python
# LeetCode 70. Climbing Stairs
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        每次可爬 1 或 2 階，到第 n 階有幾種方法。dp[i] = dp[i-1] + dp[i-2]，可壓成兩變數。
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
