# Valid Parentheses

- **LeetCode:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

判斷字串是否為合法的括號配對（僅含 `()[]{}`，且左右正確對應、巢狀正確）。

## 思路

- **Stack：** 遇到左括號就 push；遇到右括號則檢查 stack 頂是否為對應左括號，是則 pop，否則無效。最後 stack 需為空。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Stack（堆疊）
- **演算法:** 括號匹配
