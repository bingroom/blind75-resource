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
