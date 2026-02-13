# Find Median from Data Stream

- **LeetCode:** [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

支援 addNum(num) 與 findMedian()，回傳目前加入的數字的中位數。

## 思路

- **兩半堆：** 用「最大堆」存較小一半、「最小堆」存較大一半，並維持 lo 大小 ≥ hi 且最多多 1。中位數即 lo 頂（奇數個）或 (lo 頂 + hi 頂)/2（偶數個）。Python 用負值模擬最大堆。

## 時間 / 空間複雜度

- **時間:** addNum O(log n)，findMedian O(1)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Heap、兩個堆維護中位數
- **演算法:** 動態中位數
