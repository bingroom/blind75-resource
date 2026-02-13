# Set Matrix Zeroes

- **LeetCode:** [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

若矩陣某格為 0，將該行該列全部設為 0，要求 O(1) 額外空間（in-place）。

## 思路

- **用第一行、第一列當標記：** 先記錄第一行/第一列是否原本就有 0。然後用 matrix[r][0] 與 matrix[0][c] 標記第 r 行、第 c 列是否要變 0，最後根據標記填 0，再根據一開始的記錄處理第一行/列。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** In-place 標記
