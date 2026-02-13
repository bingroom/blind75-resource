# Number of 1 Bits

- **LeetCode:** [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

回傳無符號整數二進位表示中 1 的個數（Hamming weight）。

## 思路

- **n & (n - 1)** 會把 n 最右邊的 1 變成 0。重複直到 n 為 0，次數即為 1 的個數。

## 時間 / 空間複雜度

- **時間:** O(1)（位元數常數，例如 32）。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Bit Manipulation、Brian Kernighan's algorithm
