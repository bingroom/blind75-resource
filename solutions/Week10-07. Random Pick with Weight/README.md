# Random Pick with Weight

**Topic:** Binary Search

## Problem Description
Given an array `w` where `w[i]` is the weight of index `i`, implement `pickIndex()` which randomly picks an index proportional to its weight.


## Solution

```python
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
```

## Approach
Build a prefix sum array. To pick an index, generate a random integer in `[1, total_weight]` and binary search for the leftmost prefix sum that is >= that value. The prefix sum partitions the number line into segments proportional to the weights.

## Complexity
- **Time:** O(n) for initialization, O(log n) for `pickIndex`
- **Space:** O(n) for the prefix sum array
