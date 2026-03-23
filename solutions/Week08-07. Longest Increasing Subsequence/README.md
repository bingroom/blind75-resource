# Longest Increasing Subsequence

**Topic:** Dynamic Programming

- **LeetCode:** [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer array `nums`, return *the length of the longest **strictly increasing ******subsequence***.

 

**Example 1:**

```

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

```

**Example 2:**

```

Input: nums = [0,1,0,3,2,3]
Output: 4

```

**Example 3:**

```

Input: nums = [7,7,7,7,7,7,7]
Output: 1

```

 

**Constraints:**

	- `1 <= nums.length <= 2500`

	- `-10^4 <= nums[i] <= 10^4`

 

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## Solution

```python
# LeetCode 300. Longest Increasing Subsequence
# 時間複雜度: O(n²) 或 O(n log n) 二分  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        求最長嚴格遞增子序列長度。法二：維護「長度為 i 的 LIS 最小結尾」的陣列，用二分插入。
        """
        tails = []
        for x in nums:
            i = bisect.bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)

```

## 思路

- **DP + 二分：** 維護 `tails[i]` = 長度為 i+1 的遞增子序列的「最小結尾值」。遍歷 x 時用二分找第一個 ≥ x 的位置，替換或追加，最後 len(tails) 即為答案。

## 時間 / 空間複雜度

- **時間:** O(n log n)。
- **空間:** O(n)。

## 相關閱讀

- **演算法:** DP、Binary Search、Patience Sorting
