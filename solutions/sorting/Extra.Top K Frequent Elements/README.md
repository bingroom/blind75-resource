# Top K Frequent Elements

- **LeetCode:** [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

 

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

**Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

	- `k` is in the range `[1, the number of unique elements in the array]`.

	- It is **guaranteed** that the answer is **unique**.

 

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solution

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

## 思路

- **Counter + Min-Heap：** 先計數，再維護大小為 k 的 min-heap（以頻率為鍵），遍歷時若超過 k 個就 pop 最小；最後 heap 中即為前 k 大頻率對應的數。或使用桶排序（頻率當桶）可 O(n)。

## 時間 / 空間複雜度

- **時間:** O(n log k)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Heap、Counter
- **演算法:** Top K、Quick Select 可選
