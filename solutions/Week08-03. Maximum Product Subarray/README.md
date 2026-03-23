# Maximum Product Subarray

**Topic:** Dynamic Programming

- **LeetCode:** [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

 

**Example 1:**

```

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

```

**Example 2:**

```

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

```

 

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-10 <= nums[i] <= 10`

	- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

## Solution

```python
# LeetCode 152. Maximum Product Subarray
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        求連續子陣列的最大乘積。負數會讓「最小」變「最大」，故同時維護 max 與 min。
        """
        if not nums:
            return 0
        # 以當前位置結尾的：最大乘積、最小乘積（負數乘最小會變大）
        cur_max = cur_min = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            # 若 x<0，max 與 min 會互換，所以用 x 一起乘完再取 max/min
            cand = (cur_max * x, cur_min * x, x)
            cur_max = max(cand)
            cur_min = min(cand)
            best = max(best, cur_max)
        return best

```

## 思路

- 負數會讓「最小乘積」在再乘一個負數時變成「最大」，所以要同時維護「以目前位置結尾的」最大與最小乘積。
- 候選有三：`cur_max * x`、`cur_min * x`、`x`（從這裡重啟）。用三者更新 `cur_max`、`cur_min`，並用 `cur_max` 更新答案。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Kadane 變型、動態規劃
