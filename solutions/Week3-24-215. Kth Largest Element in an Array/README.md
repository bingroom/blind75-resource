# Kth Largest Element in an Array

**Topic:** Heap
- **LeetCode 連結:** [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- **難度:** Medium

## 題目描述

給定一個未排序的整數陣列，找出第 k 大的元素。

## 解題思路

1. 使用最小堆（min-heap）維護 k 個最大元素。
2. 遍歷陣列，將元素加入堆中。
3. 堆頂即為第 k 大的元素。

## 程式碼

```python
# LeetCode 215. Kth Largest Element in an Array
# Time: O(n log k)  Space: O(k)

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```

## 複雜度分析

- **時間複雜度:** O(n) average, O(n^2) worst case
- **空間複雜度:** O(1) extra space (in-place partitioning, tail recursion)
