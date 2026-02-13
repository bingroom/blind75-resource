# Linked List Cycle

- **LeetCode:** [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

判斷單向鏈表是否有環。

## 思路

- **Floyd 龜兔賽跑：** 快指針每次走 2 步、慢指針 1 步，若有環則必會相遇；若快指針走到 None 則無環。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Floyd Cycle Detection
