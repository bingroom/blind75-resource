# Sliding Window Maximum

**Topic:** Array
- **LeetCode 連結:** [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- **難度:** Hard

## 題目描述

給定一個整數陣列和滑動視窗大小 k，回傳每個視窗位置的最大值。

## 解題思路

1. 使用單調遞減雙端佇列（deque），儲存索引。
2. 移除超出視窗範圍的索引（從前端）。
3. 維護遞減順序：新元素大於佇列尾端時，從尾端移除較小的元素。
4. 視窗形成後，佇列前端即為當前視窗的最大值。

## 程式碼

```python
# LC 239. Sliding Window Maximum (Hard)
# https://leetcode.com/problems/sliding-window-maximum/
# Monotonic deque approach

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # monotonic decreasing deque of indices
        result = []

        for i, num in enumerate(nums):
            # Remove indices that have fallen out of the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order: remove smaller elements from back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)

            # Start recording results once we have a full window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
```

## 複雜度分析

- **時間複雜度:** O(n) -- each element is added and removed from the deque at most once
- **空間複雜度:** O(k) for the deque
