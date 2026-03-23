# Design Hit Counter

**Topic:** Queue
- **LeetCode 連結:** [362. Design Hit Counter](https://leetcode.com/problems/design-hit-counter/)
- **難度:** Medium

## 題目描述

設計一個點擊計數器，記錄過去 300 秒內的點擊次數。支援 hit（記錄點擊）和 getHits（查詢點擊數）兩個操作。

## 解題思路

1. 使用佇列（deque）儲存每次點擊的時間戳。
2. hit 方法將時間戳加入佇列。
3. getHits 方法移除所有超過 300 秒的舊記錄，回傳佇列長度。

## 程式碼

```python
# LeetCode 362. Design Hit Counter
# Time: O(1) amortized hit, O(n) worst-case getHits  Space: O(n)

from collections import deque


class HitCounter:
    def __init__(self):
        self.queue = deque()  # stores timestamps of hits

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Remove hits older than 300 seconds
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        return len(self.queue)
```

## 複雜度分析

- **時間複雜度:** O(1) amortized for `hit`, O(n) worst case for `getHits` (but each element is popped at most once)
- **空間複雜度:** O(n) where n is the number of hits in the last 300 seconds
