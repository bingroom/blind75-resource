# Random Pick with Weight

**Topic:** Math
- **LeetCode 連結:** [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)
- **難度:** Medium

## 題目描述

給定一個正整數權重陣列 w，實作 pickIndex 方法，以權重比例隨機回傳索引。

## 解題思路

1. 建構前綴和陣列。
2. 在 [1, 總和] 範圍內產生隨機數。
3. 使用二分搜尋在前綴和陣列中找到隨機數對應的索引。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) for initialization, O(log n) for `pickIndex`
- **空間複雜度:** O(n) for the prefix sum array
