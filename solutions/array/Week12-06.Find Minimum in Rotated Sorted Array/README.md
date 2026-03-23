# Find Minimum in Rotated Sorted Array

- **LeetCode:** [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

	- `[4,5,6,7,0,1,2]` if it was rotated `4` times.

	- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n) time`.

 

**Example 1:**

```

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

```

**Example 2:**

```

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

```

**Example 3:**

```

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5000`

	- `-5000 <= nums[i] <= 5000`

	- All the integers of `nums` are **unique**.

	- `nums` is sorted and rotated between `1` and `n` times.

## Solution

```python
# LeetCode 153. Find Minimum in Rotated Sorted Array
# 時間複雜度: O(log n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        旋轉過的有序陣列（無重複），找最小值。用二分搜：比較 mid 與 right 決定往左或往右。
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # 若 nums[mid] > nums[hi]，最小值在右半 (mid+1 ~ hi)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                # 否則在左半或就是 mid（含 mid）
                hi = mid
        return nums[lo]

```

## 思路

- **二分搜尋：** 比較 `nums[mid]` 與 `nums[hi]`。若 `nums[mid] > nums[hi]`，表示最小值在右半段；否則在左半段或就是 mid。收斂到 `lo == hi` 即為最小值位置。

## 時間 / 空間複雜度

- **時間:** O(log n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Binary Search（二分搜尋）、Rotated Sorted Array
