# Unique Paths

**Topic:** Dynamic Programming

- **LeetCode:** [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```

Input: m = 3, n = 7
Output: 28

```

**Example 2:**

```

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

```

 

**Constraints:**

	- `1 <= m, n <= 100`

## Solution

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

## 思路

- **DP：** dp[i][j] = 到 (i,j) 的路徑數 = dp[i-1][j] + dp[i][j-1]。可壓成一行，從左到右更新。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** Dynamic Programming、網格路徑計數
