# Maximum Subarray

**Topic:** Dynamic Programming
- **LeetCode 連結:** [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- **難度:** Medium

## 題目描述

給定一個整數陣列 `nums`，找出其中連續子陣列（至少包含一個元素）的最大和，並回傳該最大和。

## 解題思路

1. 使用 Kadane 演算法，維護「以當前位置結尾的最大子陣列和」`cur` 及「全域最大和」`best`。
2. 遍歷陣列，對每個元素決定：接續前面的子陣列（`cur + nums[i]`）或從當前元素重新開始（`nums[i]`），取較大者。
3. 每步更新全域最大和 `best`。
4. 遍歷結束後回傳 `best`。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
