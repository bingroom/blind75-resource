# Climbing Stairs

**Topic:** Dynamic Programming

- **LeetCode:** [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

 

**Example 1:**

```

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

**Example 2:**

```

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

 

**Constraints:**

	- `1 <= n <= 45`

## Solution

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

## 思路

- **DP：** 到第 i 階的方法數 = 從 i-1 爬一步 + 從 i-2 爬兩步，即 `dp[i] = dp[i-1] + dp[i-2]`。可只保留前兩項，空間 O(1)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Dynamic Programming、Fibonacci 數列
