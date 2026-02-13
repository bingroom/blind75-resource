# Palindromic Substrings

- **LeetCode:** [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

計算字串中「迴文子字串」的總個數（相同字元不同位置算不同子字串）。

## 思路

- **中心擴展：** 與「最長迴文子字串」相同，以每個位置為奇/偶中心向外擴展，每成功擴展一格就多一個迴文，累加 count。

## 時間 / 空間複雜度

- **時間:** O(n²)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Expand Around Center
