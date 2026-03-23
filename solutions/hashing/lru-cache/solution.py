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
