# Product of Array Except Self

- **LeetCode:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

回傳一新陣列，其中 `output[i]` = 除 `nums[i]` 外所有元素的乘積。限制：不可用除法，且希望額外空間 O(1)（不含輸出）。

## 思路

- `output[i]` = (i 左邊所有數的乘積) × (i 右邊所有數的乘積)。
- 先從左到右掃一遍，在 `out[i]` 存「左乘積」；再從右到左掃一遍，乘上「右乘積」。兩遍即可，且只多用一個變數（left/right）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1) 額外（輸出不計）。

## 相關閱讀

- **演算法:** 前綴/後綴乘積 (prefix/suffix product)、兩遍掃描
