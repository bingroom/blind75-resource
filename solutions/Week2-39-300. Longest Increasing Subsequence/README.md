# Longest Increasing Subsequence

**Topic:** Dynamic Programming
- **LeetCode 連結:** [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- **難度:** Medium

## 題目描述

給定一個整數陣列，找出最長嚴格遞增子序列的長度。子序列不需要連續，但須保持原始順序。

## 解題思路

1. 維護一個陣列 tails，tails[i] 表示長度為 i+1 的遞增子序列的最小結尾元素。
2. 遍歷每個數字，使用二分搜尋在 tails 中找到第一個大於等於它的位置。
3. 若位置在末尾，將數字追加到 tails（延伸最長子序列）。
4. 否則替換該位置的值（保持結尾盡可能小，有利於後續延伸）。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n log n)。
- **空間複雜度:** O(n)。
