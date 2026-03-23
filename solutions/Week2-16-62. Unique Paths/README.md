# Unique Paths

**Topic:** Dynamic Programming
- **LeetCode 連結:** [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
- **難度:** Medium

## 題目描述

一個機器人位於 m x n 網格的左上角，每次只能向右或向下移動一步。求到達右下角共有多少條不同的路徑。

## 解題思路

1. 建立一維 DP 陣列，初始值全為 1（第一列只有一種走法）。
2. 逐列更新：dp[j] += dp[j-1]，代表從上方和左方來的路徑數之和。
3. 遍歷完所有列後，dp[n-1] 即為答案。

## 程式碼

```python
# LeetCode 62. Unique Paths
# 時間複雜度: O(m * n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        從左上到右下，只能向右或向下，求路徑數。dp[j] 可壓成一行，dp[j] += dp[j-1]。
        """
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]
```

## 複雜度分析

- **時間複雜度:** O(m×n)。
- **空間複雜度:** O(n)。
