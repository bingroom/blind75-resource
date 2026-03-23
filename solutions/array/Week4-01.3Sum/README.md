# 3Sum

- **LeetCode:** [15. 3Sum](https://leetcode.com/problems/3sum/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

**Example 1:**

```

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```

**Example 2:**

```

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

```

**Example 3:**

```

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

```

 

**Constraints:**

	- `3 <= nums.length <= 3000`

	- `-10^5 <= nums[i] <= 10^5`

## Solution

```python
# LeetCode 15. 3Sum
# 時間複雜度: O(n²)  空間複雜度: O(1) 不含排序
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        找出所有和為 0 的三元組 (不重複)。排序 + 枚舉第一個數，其餘用雙指針做 2Sum。
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            # 避免重複：若與上一個數相同則跳過
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 在 i+1..n-1 之間用雙指針找兩數和 = -nums[i]
            lo, hi = i + 1, n - 1
            target = -nums[i]
            while lo < hi:
                s = nums[lo] + nums[hi]
                if s == target:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    # 跳過重複的 nums[lo]
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif s < target:
                    lo += 1
                else:
                    hi -= 1
        return ans

```

## 思路

- **排序**後，枚舉第一個數 `nums[i]`，在 `i+1..n-1` 用**雙指針**找兩數和 = `-nums[i]`（即 2Sum）。重複的數用「與前一個相同就跳過」來去重。

## 時間 / 空間複雜度

- **時間:** O(n²)（排序 O(n log n) + 枚舉 O(n) × 雙指針 O(n)）。
- **空間:** O(1) 額外（不含輸出；排序可能 O(log n) 遞迴棧）。

## 相關閱讀

- **演算法:** Two Pointers、2Sum 變型、排序
