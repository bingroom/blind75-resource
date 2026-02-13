# Spiral Matrix

- **LeetCode:** [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

依螺旋順序（右上左下）回傳矩陣所有元素。

## 思路

- **邊界法：** 維護 top/bottom/left/right，依序輸出上邊、右邊、下邊、左邊，每輪後收縮邊界，注意最後兩邊可能只剩一行/一列需判斷。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(1) 額外（不含輸出）。

## 相關閱讀

- **演算法:** 邊界收縮、模擬
