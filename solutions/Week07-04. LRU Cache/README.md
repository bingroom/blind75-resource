# LRU Cache

**Topic:** Hashing

- **LeetCode:** [146. LRU Cache](https://leetcode.com/problems/lru-cache/)

## Problem Description

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement `LRUCache` with `get(key)` and `put(key, value)`, both running in O(1) average time. When the cache exceeds its capacity, evict the least recently used key before inserting a new one.


## Solution

```python
# LeetCode 146. LRU Cache
# Time: O(1) per get/put  Space: O(capacity)

from collections import OrderedDict


class LRUCache:
    """
    Least Recently Used cache backed by OrderedDict.
    OrderedDict.move_to_end() and popitem(last=False) give O(1) operations.
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)      # mark as most recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # update recency
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # evict least recently used
```

## Approach

Use Python's `OrderedDict`, which combines a hash map with a doubly-linked list internally:

1. **get(key):** If the key exists, move it to the end (most recent) and return its value. Otherwise return -1.
2. **put(key, value):** If the key already exists, move it to the end. Set the value. If the size exceeds capacity, pop the first item (least recently used) with `popitem(last=False)`.

This gives O(1) for both operations because `OrderedDict.move_to_end()` and `popitem()` are O(1).

## Complexity

- **Time:** O(1) per `get` and `put` call.
- **Space:** O(capacity) for storing up to `capacity` key-value pairs.
