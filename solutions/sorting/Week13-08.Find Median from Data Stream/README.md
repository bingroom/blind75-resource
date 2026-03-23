# Find Median from Data Stream

- **LeetCode:** [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

	- For example, for `arr = [2,3,4]`, the median is `3`.

	- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

	- `MedianFinder()` initializes the `MedianFinder` object.

	- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.

	- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

 

**Example 1:**

```

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

```

 

**Constraints:**

	- `-10^5 <= num <= 10^5`

	- There will be at least one element in the data structure before calling `findMedian`.

	- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

 

**Follow up:**

	- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

	- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## Solution

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

## 思路

- **兩半堆：** 用「最大堆」存較小一半、「最小堆」存較大一半，並維持 lo 大小 ≥ hi 且最多多 1。中位數即 lo 頂（奇數個）或 (lo 頂 + hi 頂)/2（偶數個）。Python 用負值模擬最大堆。

## 時間 / 空間複雜度

- **時間:** addNum O(log n)，findMedian O(1)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Heap、兩個堆維護中位數
- **演算法:** 動態中位數
