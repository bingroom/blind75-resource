# 3Sum

**Topic:** Array
- **LeetCode 連結:** [15. 3Sum](https://leetcode.com/problems/3sum/)
- **難度:** Medium

## 題目描述

給定一個整數陣列 `nums`，找出所有不重複的三元組 `[nums[i], nums[j], nums[k]]` 使得三數之和為 0。結果中不可包含重複的三元組。

## 解題思路

1. 先將陣列排序。
2. 枚舉第一個數 `nums[i]`，跳過與前一個相同的數以避免重複。
3. 對剩餘部分使用雙指針（`lo` 和 `hi`）尋找兩數之和等於 `-nums[i]`。
4. 若三數之和為 0，記錄結果並跳過重複值；若和太小則左指針右移；若和太大則右指針左移。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n²)（排序 O(n log n) + 枚舉 O(n) × 雙指針 O(n)）。
- **空間複雜度:** O(1) 額外（不含輸出；排序可能 O(log n) 遞迴棧）。
