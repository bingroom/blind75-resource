# Maximum Product Subarray

**Topic:** Dynamic Programming
- **LeetCode 連結:** [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- **難度:** Medium

## 題目描述

給定一個整數陣列，找出乘積最大的連續子陣列，回傳其乘積。陣列中可能包含正數、負數和零。

## 解題思路

1. 同時維護以當前位置結尾的最大乘積和最小乘積（負數乘以最小值可能變成最大值）。
2. 對每個元素，計算三個候選值：cur_max * x、cur_min * x、x 本身。
3. 從候選值中取最大和最小，更新 cur_max 和 cur_min。
4. 持續更新全域最大乘積。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
