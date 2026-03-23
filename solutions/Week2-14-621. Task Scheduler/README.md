# Task Scheduler

**Topic:** Heap
- **LeetCode 連結:** [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- **難度:** Medium

## 題目描述

給定一組任務和冷卻間隔 n，相同任務之間至少需要間隔 n 個時間單位。求完成所有任務所需的最少時間單位數。

## 解題思路

1. 統計每個任務的出現頻率，找出最高頻率 max_freq。
2. 計算有多少任務具有最高頻率（max_count）。
3. 套用公式：(max_freq - 1) * (n + 1) + max_count。
4. 答案取上述公式和任務總數的較大值（當任務種類多到不需閒置時）。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) where n is the number of tasks
- **空間複雜度:** O(1) -- at most 26 task types
