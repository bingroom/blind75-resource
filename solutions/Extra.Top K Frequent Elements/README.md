# Top K Frequent Elements

**Topic:** Unknown
- **LeetCode 連結:** [0. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **難度:** Medium

## 題目描述

給定一個整數陣列和整數 k，回傳出現頻率前 k 高的元素。

## 解題思路

1. 使用 Counter 計算每個元素的出現次數。
2. 建立大小為 k 的最小堆，依頻率排序。
3. 遍歷所有元素，堆超過 k 時彈出最小的。
4. 堆中剩餘的 k 個元素即為答案。

## 程式碼

```python
# LeetCode 347. Top K Frequent Elements
# 時間複雜度: O(n log k) 或 O(n) 桶排序  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        回傳出現頻率前 k 高的元素。Counter 計數後用 min-heap 維持 k 個最大頻率，或桶排序。
        """
        count = Counter(nums)
        # min-heap 存 (頻率, 數值)，維持 size k，最後留下的是前 k 大
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]
```

## 複雜度分析

- **時間複雜度:** O(n log k)。
- **空間複雜度:** O(n)。
