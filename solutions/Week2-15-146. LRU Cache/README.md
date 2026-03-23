# LRU Cache

**Topic:** Linked List
- **LeetCode 連結:** [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
- **難度:** Medium

## 題目描述

設計一個最近最少使用（LRU）快取機制，支援 get 和 put 操作，兩者皆需在 O(1) 時間複雜度內完成。當快取容量達到上限時，移除最久未使用的項目。

## 解題思路

1. 使用 OrderedDict 同時維護插入順序和 O(1) 查找。
2. get 操作：若 key 存在，使用 move_to_end 將其標記為最近使用，回傳值；否則回傳 -1。
3. put 操作：若 key 已存在，更新值並移到末端；若不存在則新增。
4. 新增後若超過容量，使用 popitem(last=False) 移除最前面（最久未使用）的項目。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(1) per `get` and `put` call.
- **空間複雜度:** O(capacity) for storing up to `capacity` key-value pairs.
