# Valid Parentheses

**Topic:** Stack
- **LeetCode 連結:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- **難度:** Easy

## 題目描述

給定一個只包含 `(`、`)`、`{`、`}`、`[`、`]` 的字串，判斷括號是否正確配對。每個左括號必須有對應的同類型右括號，且順序正確。

## 解題思路

1. 使用堆疊（stack）來追蹤尚未配對的左括號。
2. 遍歷字串，遇到左括號則推入堆疊。
3. 遇到右括號時，檢查堆疊頂端是否為對應的左括號；若不是或堆疊為空，回傳 `False`。
4. 遍歷結束後，若堆疊為空表示所有括號正確配對，回傳 `True`。

## 程式碼

```python
# LeetCode 20. Valid Parentheses
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def isValid(self, s: str) -> bool:
        """
        判斷括號是否正確配對。用 stack：左括號 push，右括號 pop 並檢查是否對應。
        """
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in pair:
                if not stack or stack[-1] != pair[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(n)。
