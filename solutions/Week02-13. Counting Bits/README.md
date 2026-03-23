# Counting Bits

**Topic:** Bit Manipulation

- **LeetCode:** [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer `n`, return *an array *`ans`* of length *`n + 1`* such that for each *`i`* *(`0 <= i <= n`)*, *`ans[i]`* is the **number of ***`1`***'s** in the binary representation of *`i`.

 

**Example 1:**

```

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

```

**Example 2:**

```

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

```

 

**Constraints:**

	- `0 <= n <= 10^5`

 

**Follow up:**

	- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?

	- Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?

## Solution

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

## 思路

- **DP：** `ans[i] = ans[i >> 1] + (i & 1)`。即「右移一位的 1 的個數」加上「最低位是否為 1」。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1) 額外（不含輸出陣列）。

## 相關閱讀

- **演算法:** Dynamic Programming、Bit Manipulation
