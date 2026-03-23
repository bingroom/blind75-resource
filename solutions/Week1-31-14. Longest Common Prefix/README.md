# Longest Common Prefix

**Topic:** String
- **LeetCode 連結:** [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- **難度:** Easy

## 題目描述

給定一組字串，找出它們的最長公共前綴。若不存在公共前綴則回傳空字串。

## 解題思路

1. 以第一個字串為基準，逐字元比較。
2. 對每個位置，檢查所有字串在該位置的字元是否相同。
3. 若遇到不同字元或超出某字串長度，回傳已匹配的前綴。

## 程式碼

```python
# LeetCode 14. Longest Common Prefix
# Time: O(S) where S = sum of all characters  Space: O(1)

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Compare characters column by column
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return strs[0][:i]
        return strs[0]
```

## 複雜度分析

- **時間複雜度:** O(S) where S is the sum of all characters in all strings
- **空間複雜度:** O(1)
