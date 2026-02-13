# Merge K Sorted Lists

- **LeetCode:** [23. Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

合併 k 條已排序鏈表為一條。

## 思路

- **Min-Heap：** 把每條鏈表的頭節點放入 heap，每次 pop 最小值接到結果鏈表，並把該節點的 next（若有）push 進 heap。需在 heap 中加索引以處理同值比較。

## 時間 / 空間複雜度

- **時間:** O(N log k)，N 為總節點數。
- **空間:** O(k)。

## 相關閱讀

- **資料結構:** Heap、Linked List
- **演算法:** K-way Merge
