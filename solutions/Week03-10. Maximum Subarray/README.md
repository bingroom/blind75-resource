# Maximum Subarray

**Topic:** Array

- **LeetCode:** [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.

 

**Example 1:**

```

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

**Example 2:**

```

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

**Example 3:**

```

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Solution

```python
# LeetCode 53. Maximum Subarray (Kadane's Algorithm)
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        求連續子陣列的最大和（至少取一個元素）。
        Kadane：以「以當前位置結尾」的最大和來推，要麼接上前面，要麼只取自己。
        """
        if not nums:
            return 0
        # cur = 以當前位置為結尾的最大子陣列和
        cur = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            # 要麼接上前面 (cur + nums[i])，要麼從這裡重新開始 (nums[i])
            cur = max(nums[i], cur + nums[i])
            best = max(best, cur)
        return best

```

## 思路

- **Kadane 演算法：** 定義 `cur` = 以「目前位置」為結尾的最大子陣列和。每次要麼接上前面 (`cur + nums[i]`)，要麼從這裡重啟 (`nums[i]`)，取較大者；再以 `best` 記錄全域最大。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Kadane's Algorithm、動態規劃 (DP) 一維
