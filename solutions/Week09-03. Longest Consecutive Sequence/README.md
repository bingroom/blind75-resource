# Longest Consecutive Sequence

**Topic:** Hashing

- **LeetCode:** [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

 

**Example 1:**

```

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

**Example 2:**

```

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

**Example 3:**

```

Input: nums = [1,0,1,2]
Output: 3

```

 

**Constraints:**

	- `0 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## Solution

```python
# LeetCode 128. Longest Consecutive Sequence
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        求未排序陣列中最長連續數字序列的長度（如 1,2,3,4）。用 set 存所有數，只從「序列起點」開始數長度。
        """
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                cur = x
                while cur in s:
                    cur += 1
                best = max(best, cur - x)
        return best

```

## 思路

- **Set：** 將所有數放入 set。只從「序列起點」開始計數（即 x-1 不在 set 的 x），往右數到不在 set 為止，更新最長長度。這樣每數只被起點數一次，O(n)。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Set、Hash Table
- **演算法:** 只從邊界擴展避免重複
