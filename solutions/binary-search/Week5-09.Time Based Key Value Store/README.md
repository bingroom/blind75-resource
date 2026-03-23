# Time Based Key-Value Store

## Problem Description
Design a data structure that stores key-value pairs with timestamps. Support `set(key, value, timestamp)` and `get(key, timestamp)` where `get` returns the value with the largest timestamp less than or equal to the given timestamp.


## Solution

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

## Approach
Use a dictionary mapping each key to a list of `(timestamp, value)` pairs. Since `set` is called with strictly increasing timestamps, the list is already sorted. For `get`, use `bisect_right` to find the insertion point for the query timestamp, then return the value at the position just before it.

## Complexity
- **Time:** O(1) for `set`, O(log n) for `get` where n is the number of entries for a key
- **Space:** O(n) total entries stored
