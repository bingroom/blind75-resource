# Valid Palindrome

- **LeetCode:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **NeetCode 練習（本題可直接提交 AC）：** [Valid Palindrome - Blind 75](https://neetcode.io/problems/is-palindrome?list=blind75)

## 題意

給定字串，只考慮**英數字**（A–Z, a–z, 0–9），忽略大小寫與其他字元，判斷是否為迴文（正讀反讀相同）。

## 思路

- **雙指針：** 左指針從頭、右指針從尾往內。若當前字元非英數字則移動跳過；否則比較轉小寫後是否相同，不同則回傳 False。相遇或交錯後回傳 True。

## 時間 / 空間複雜度

- **時間:** O(n)，每個字元最多被訪問兩次。
- **空間:** O(1)，只使用兩個指針與常數變數。

## 相關閱讀

- **演算法:** Two Pointers（雙指針）
- **字串:** 字元判斷 `isalnum()`、大小寫 `lower()`
