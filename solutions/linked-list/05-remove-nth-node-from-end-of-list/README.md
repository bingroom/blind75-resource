# Remove Nth Node From End of List

- **LeetCode:** [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

刪除單向鏈表的**倒數第 n 個**節點，一次遍歷、O(1) 額外空間。

## 思路

- **快慢指針：** 快指針先走 n+1 步（與慢指針間隔 n 個節點），再一起走直到快指針到 None，此時慢指針.next 即為倒數第 n 個，刪除即可。用 dummy 處理刪頭情況。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Two Pointers、Dummy Head
