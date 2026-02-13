# Search in Rotated Sorted Array

- **LeetCode:** [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of *`target`* if it is in *`nums`*, or *`-1`* if it is not in *`nums`.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

```

**Example 3:**

```
Input: nums = [1], target = 0
Output: -1

```

 

**Constraints:**

	- `1 <= nums.length <= 5000`

	- `-10^4 <= nums[i] <= 10^4`

	- All values of `nums` are **unique**.

	- `nums` is an ascending array that is possibly rotated.

	- `-10^4 <= target <= 10^4`

## Solution

```python
# LeetCode 33. Search in Rotated Sorted Array
# 時間複雜度: O(log n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        在旋轉過的有序陣列（無重複）中找 target 的索引，沒有則回傳 -1。
        二分：先判斷左半或右半哪一段是有序的，再判斷 target 是否落在該段內。
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            # 左半 [lo..mid] 為有序
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # 右半 [mid..hi] 為有序
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

```

## 思路

- **二分搜尋：** 每次看 `nums[lo]` 與 `nums[mid]` 的關係，判斷「左半 [lo..mid]」或「右半 [mid..hi]」哪一段是連續有序的；再判斷 target 是否落在該段內，決定往左或往右縮小範圍。

## 時間 / 空間複雜度

- **時間:** O(log n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Binary Search、Rotated Sorted Array
