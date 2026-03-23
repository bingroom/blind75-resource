# LRU Cache

- **LeetCode:** [146. LRU Cache](https://leetcode.com/problems/lru-cache/)

## Problem Description

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement `LRUCache` with `get(key)` and `put(key, value)`, both running in O(1) average time. When the cache exceeds its capacity, evict the least recently used key before inserting a new one.

## Approach

Use Python's `OrderedDict`, which combines a hash map with a doubly-linked list internally:

1. **get(key):** If the key exists, move it to the end (most recent) and return its value. Otherwise return -1.
2. **put(key, value):** If the key already exists, move it to the end. Set the value. If the size exceeds capacity, pop the first item (least recently used) with `popitem(last=False)`.

This gives O(1) for both operations because `OrderedDict.move_to_end()` and `popitem()` are O(1).

## Complexity

- **Time:** O(1) per `get` and `put` call.
- **Space:** O(capacity) for storing up to `capacity` key-value pairs.
