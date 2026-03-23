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
