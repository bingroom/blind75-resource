# Merge Two Sorted Lists

- **LeetCode:** [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

合併兩條已排序的單向鏈表，回傳一條新的已排序鏈表。

## 思路

- **Dummy 頭 + 雙指針：** 用 dummy 簡化邊界，每次比較兩鏈表頭，取較小者接到 cur，並移動該鏈表指針。最後接上剩餘部分。

## 時間 / 空間複雜度

- **時間:** O(m+n)。
- **空間:** O(1)（不計新節點）。

## 相關閱讀

- **資料結構:** Linked List、Merge
