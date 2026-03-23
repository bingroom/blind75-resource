# Number of 1 Bits

**Topic:** Bit Manipulation

- **LeetCode:** [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

**Example 1:**

**Input:** n = 11

**Output:** 3

**Explanation:**

The input binary string **1011** has a total of three set bits.

**Example 2:**

**Input:** n = 128

**Output:** 1

**Explanation:**

The input binary string **10000000** has a total of one set bit.

**Example 3:**

**Input:** n = 2147483645

**Output:** 30

**Explanation:**

The input binary string **1111111111111111111111111111101** has a total of thirty set bits.

 

**Constraints:**

	- `1 <= n <= 2^31 - 1`

 
**Follow up:** If this function is called many times, how would you optimize it?

## Solution

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

## 思路

- **n & (n - 1)** 會把 n 最右邊的 1 變成 0。重複直到 n 為 0，次數即為 1 的個數。

## 時間 / 空間複雜度

- **時間:** O(1)（位元數常數，例如 32）。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Bit Manipulation、Brian Kernighan's algorithm
