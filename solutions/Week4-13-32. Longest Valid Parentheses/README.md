# Longest Valid Parentheses

**Topic:** Stack
- **LeetCode 連結:** [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
- **難度:** Hard

## 題目描述

給定一個只包含 '(' 和 ')' 的字串，找出最長合法括號子字串的長度。

## 解題思路

1. 使用堆疊存放索引，底部放置邊界標記（初始為 -1）。
2. 遇到 '(' 時將索引推入堆疊。
3. 遇到 ')' 時彈出堆疊頂端：若堆疊為空則推入當前索引作為新邊界，否則用當前索引減去堆疊頂端更新最大長度。

## 程式碼

```python
# LeetCode 32. Longest Valid Parentheses
# Time: O(n)  Space: O(n)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack stores indices; bottom of stack is the boundary marker
        stack = [-1]  # initial boundary
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # No matching '(' -- push current index as new boundary
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(n)
