# Time Based Key-Value Store

**Topic:** Binary Search
- **LeetCode 連結:** [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
- **難度:** Medium

## 題目描述

設計一個基於時間戳的鍵值儲存結構，支援在特定時間戳儲存鍵值對，以及查詢某個鍵在指定時間戳或之前最近的值。若沒有符合條件的值則回傳空字串。

## 解題思路

1. 使用雜湊表將每個 key 對應到一個 (timestamp, value) 的有序列表。
2. set 操作直接將 (timestamp, value) 追加到列表末端（時間戳遞增保證有序）。
3. get 操作使用二分搜尋（bisect_right），找到小於等於指定時間戳的最大時間戳對應的值。
4. 若找不到符合條件的時間戳，回傳空字串。

## 程式碼

```python
# LeetCode 981. Time Based Key-Value Store
# Time: O(1) set, O(log n) get  Space: O(n)

from collections import defaultdict
import bisect


class TimeMap:
    def __init__(self):
        # key -> list of (timestamp, value) pairs, timestamps are strictly increasing
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        pairs = self.store[key]
        # Binary search for the rightmost timestamp <= given timestamp
        idx = bisect.bisect_right(pairs, (timestamp, chr(127))) - 1
        if idx < 0:
            return ""
        return pairs[idx][1]
```

## 複雜度分析

- **時間複雜度:** O(1) for `set`, O(log n) for `get` where n is the number of entries for a key
- **空間複雜度:** O(n) total entries stored
