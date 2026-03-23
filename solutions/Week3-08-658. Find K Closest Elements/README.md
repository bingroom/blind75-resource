# Find K Closest Elements

**Topic:** Heap
- **LeetCode 連結:** [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
- **難度:** Medium

## 題目描述

給定一個已排序的整數陣列、一個整數 k 和一個目標值 x，找出陣列中離 x 最近的 k 個元素，以升序回傳。

## 解題思路

1. 使用二分搜尋找到長度為 k 的視窗的左邊界，搜尋範圍為 [0, n-k]。
2. 對於候選起點 mid，比較 x - arr[mid] 和 arr[mid+k] - x。
3. 若右側元素更近，將左邊界右移；否則右邊界左移。
4. 最終左邊界即為結果視窗的起點，回傳 arr[left:left+k]。

## 程式碼

```python
# LeetCode 658. Find K Closest Elements
# Time: O(log(n - k) + k)  Space: O(1) excluding output

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary search for the left boundary of the k-length window.
        The window starts at some index in [0, n - k]. For a candidate
        start `mid`, compare the distance of arr[mid] and arr[mid + k]
        to x: if arr[mid + k] is closer (or equal), shift right.
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # Compare which side is farther from x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
```

## 複雜度分析

- **時間複雜度:** O(log(n - k) + k) -- binary search plus slicing the result.
- **空間複雜度:** O(1) -- excluding the output list.
