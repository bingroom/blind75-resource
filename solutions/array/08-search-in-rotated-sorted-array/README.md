# Search in Rotated Sorted Array

- **LeetCode:** [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

在旋轉過的有序陣列（無重複）中找 target，回傳索引，不存在則 -1。

## 思路

- **二分搜尋：** 每次看 `nums[lo]` 與 `nums[mid]` 的關係，判斷「左半 [lo..mid]」或「右半 [mid..hi]」哪一段是連續有序的；再判斷 target 是否落在該段內，決定往左或往右縮小範圍。

## 時間 / 空間複雜度

- **時間:** O(log n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Binary Search、Rotated Sorted Array
