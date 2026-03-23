# Time Based Key-Value Store

## Problem Description
Design a data structure that stores key-value pairs with timestamps. Support `set(key, value, timestamp)` and `get(key, timestamp)` where `get` returns the value with the largest timestamp less than or equal to the given timestamp.

## Approach
Use a dictionary mapping each key to a list of `(timestamp, value)` pairs. Since `set` is called with strictly increasing timestamps, the list is already sorted. For `get`, use `bisect_right` to find the insertion point for the query timestamp, then return the value at the position just before it.

## Complexity
- **Time:** O(1) for `set`, O(log n) for `get` where n is the number of entries for a key
- **Space:** O(n) total entries stored
