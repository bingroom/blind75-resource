# Find Median from Data Stream

**Topic:** Heap
- **LeetCode 連結:** [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- **難度:** Hard

## 題目描述

設計一個資料結構，支援從資料流中持續加入整數，並能在任意時刻找出目前所有已加入數字的中位數。

## 解題思路

1. 使用兩個堆：最大堆 lo 存較小的一半，最小堆 hi 存較大的一半。
2. 加入新數字時，先推入 lo，再將 lo 的堆頂移到 hi，確保 lo 的所有值都小於 hi。
3. 若 lo 的大小小於 hi，將 hi 的堆頂移回 lo，保持 lo 的大小大於等於 hi。
4. 取中位數時，若兩堆大小相同取兩堆頂的平均值；否則取 lo 的堆頂。

## 程式碼

```python
# LeetCode 295. Find Median from Data Stream
# 時間複雜度: addNum O(log n)  findMedian O(1)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

import heapq


class MedianFinder:
    def __init__(self):
        self.lo = []   # 最大堆，存較小一半（Python heapq 為最小堆，存負值）
        self.hi = []   # 最小堆，存較大一半

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0
```

## 複雜度分析

- **時間複雜度:** addNum O(log n)，findMedian O(1)。
- **空間複雜度:** O(n)。
