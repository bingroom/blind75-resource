# LeetCode 528. Random Pick with Weight
# Time: O(n) init, O(log n) pickIndex  Space: O(n)

import bisect
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        # Build prefix sum array
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # Pick a random number in [1, total], then binary search for its position
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)
