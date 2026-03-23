# Daily Temperatures

**Topic:** Stack
- **LeetCode 連結:** [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- **難度:** Medium

## 題目描述

給定一個每日溫度的陣列，回傳一個陣列，其中每個元素表示需要等幾天才能等到更高的溫度。若之後都沒有更高溫度，則該位置填 0。

## 解題思路

1. 使用單調遞減堆疊儲存尚未找到更高溫度的日期索引。
2. 遍歷每一天，若當前溫度高於堆疊頂端索引對應的溫度，則彈出並計算等待天數。
3. 將當前索引壓入堆疊。
4. 每個索引最多被壓入和彈出各一次，整體為線性時間。

## 程式碼

```python
# LC 739. Daily Temperatures (Medium)
# https://leetcode.com/problems/daily-temperatures/
# Monotonic stack approach

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # monotonic decreasing stack of indices

        for i, temp in enumerate(temperatures):
            # Pop all indices whose temperature is less than current
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)

        return answer
```

## 複雜度分析

- **時間複雜度:** O(n) -- each index is pushed and popped at most once
- **空間複雜度:** O(n)
