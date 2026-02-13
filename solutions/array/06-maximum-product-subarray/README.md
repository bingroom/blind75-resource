# Maximum Product Subarray

- **LeetCode:** [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求連續子陣列的最大乘積（至少取一個元素）。

## 思路

- 負數會讓「最小乘積」在再乘一個負數時變成「最大」，所以要同時維護「以目前位置結尾的」最大與最小乘積。
- 候選有三：`cur_max * x`、`cur_min * x`、`x`（從這裡重啟）。用三者更新 `cur_max`、`cur_min`，並用 `cur_max` 更新答案。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Kadane 變型、動態規劃
