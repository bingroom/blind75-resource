# Median of Two Sorted Arrays

**Topic:** Binary Search
- **LeetCode 連結:** [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- **難度:** Hard

## 題目描述

給定兩個已排序的整數陣列 nums1 和 nums2，找出這兩個陣列合併後的中位數。要求時間複雜度為 O(log(min(m, n)))。

## 解題思路

1. 確保在較短的陣列上進行二分搜尋。
2. 二分搜尋分割位置 i，使兩個陣列的左半部分恰好包含 (m+n+1)/2 個元素。
3. 檢查分割是否有效：左半部分的最大值不超過右半部分的最小值。
4. 若總元素數為奇數，中位數為左半部分的最大值；若為偶數，為左最大和右最小的平均值。

## 程式碼

```python
# LeetCode 4. Median of Two Sorted Arrays
# Time: O(log(min(m, n)))  Space: O(1)

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search on the shorter array to find the correct partition.
        We split both arrays so that the left half contains exactly
        (m + n + 1) // 2 elements. The partition is valid when
        max(left1, left2) <= min(right1, right2).
        """
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # partition index in nums1
            j = half - i              # partition index in nums2

            # Edge values: use -inf/+inf when a partition side is empty
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Valid partition found
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1  # move partition left in nums1
            else:
                left = i + 1   # move partition right in nums1

        return 0.0  # unreachable with valid input
```

## 複雜度分析

- **時間複雜度:** O(log(min(m, n))) -- binary search on the shorter array.
- **空間複雜度:** O(1) -- constant extra space.
