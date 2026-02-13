# Find Minimum in Rotated Sorted Array

- **LeetCode:** [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

給定旋轉過的有序陣列（無重複），求最小值。

## 思路

- **二分搜尋：** 比較 `nums[mid]` 與 `nums[hi]`。若 `nums[mid] > nums[hi]`，表示最小值在右半段；否則在左半段或就是 mid。收斂到 `lo == hi` 即為最小值位置。

## 時間 / 空間複雜度

- **時間:** O(log n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Binary Search（二分搜尋）、Rotated Sorted Array
