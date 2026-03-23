# Valid Parentheses

- **LeetCode:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	- Open brackets must be closed by the same type of brackets.

	- Open brackets must be closed in the correct order.

	- Every close bracket has a corresponding open bracket of the same type.

 

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true

**Example 3:**

**Input:** s = "(]"

**Output:** false

**Example 4:**

**Input:** s = "([])"

**Output:** true

**Example 5:**

**Input:** s = "([)]"

**Output:** false

 

**Constraints:**

	- `1 <= s.length <= 10^4`

	- `s` consists of parentheses only `'()[]{}'`.

## Solution

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

## 思路

- **Stack：** 遇到左括號就 push；遇到右括號則檢查 stack 頂是否為對應左括號，是則 pop，否則無效。最後 stack 需為空。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Stack（堆疊）
- **演算法:** 括號匹配
