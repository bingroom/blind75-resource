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
