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
