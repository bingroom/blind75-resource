# Longest Consecutive Sequence

**Topic:** Array
- **LeetCode 連結:** [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- **難度:** Medium

## 題目描述

給定一個未排序的整數陣列，找出最長連續數字序列的長度（如 1, 2, 3, 4）。要求演算法的時間複雜度為 O(n)。

## 解題思路

1. 將所有數字放入集合（set）。
2. 遍歷集合中的每個數字，只從序列的起點開始計算（即 x-1 不在集合中的數字）。
3. 從起點開始向上逐一檢查 x+1, x+2, ... 是否在集合中，計算連續長度。
4. 持續更新最長連續序列長度。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(n)。
