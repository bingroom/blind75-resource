# Task Scheduler

**Topic:** Greedy

## Problem Description
Given a list of tasks represented by characters and a cooldown interval `n`, return the minimum number of intervals the CPU needs to finish all tasks. The same task must be separated by at least `n` intervals.


## Solution

```python
# LeetCode 621. Task Scheduler
# Time: O(n)  Space: O(1)

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        # Number of tasks that have the maximum frequency
        max_count = sum(1 for v in counts.values() if v == max_freq)

        # Formula: (max_freq - 1) chunks of size (n + 1), plus max_count for the last row
        # But we need at least len(tasks) slots total
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
```

## Approach
The most frequent task dictates the schedule. Arrange the most frequent task in a grid with `(n + 1)` slots per row. The minimum time is `(max_freq - 1) * (n + 1) + max_count`, where `max_count` is how many tasks share the maximum frequency. The answer is the max of this and `len(tasks)` (when there are enough distinct tasks to fill all idle slots).

## Complexity
- **Time:** O(n) where n is the number of tasks
- **Space:** O(1) -- at most 26 task types
