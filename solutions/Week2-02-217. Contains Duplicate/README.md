# Contains Duplicate

**Topic:** Array
- **LeetCode 連結:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- **難度:** Easy

## 題目描述

給定一個整數陣列，判斷是否存在重複的元素。若任何值出現至少兩次，回傳 true；若所有元素皆不重複，回傳 false。

## 解題思路

1. 建立一個集合（set）用於記錄已遍歷過的數字。
2. 逐一遍歷陣列中的每個數字。
3. 若該數字已存在於集合中，回傳 true。
4. 否則將該數字加入集合，繼續檢查下一個。

## 程式碼

```python
# LeetCode 217. Contains Duplicate
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        判斷陣列中是否有重複元素。
        用 set 記錄已見過的數，遇過就回傳 True。
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(n)。
