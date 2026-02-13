# Decode Ways

- **LeetCode:** [91. Decode Ways](https://leetcode.com/problems/decode-ways/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

數字字串可解碼成字母（1→A, ..., 26→Z），單一數字或兩位數（10–26）皆可，求解碼方法數。

## 思路

- **DP：** 當前位置可從前一個（單字元）或前兩個（雙字元 10–26）轉移。注意 '0' 不能單獨解碼。可壓成兩變數。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Dynamic Programming、字串解碼
