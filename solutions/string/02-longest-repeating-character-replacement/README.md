# Longest Repeating Character Replacement

- **LeetCode:** [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

可將最多 k 個字元替換成任意字元，求最長「全部同一字元」的連續子字串長度。

## 思路

- **滑動視窗：** 窗內「長度 − 出現次數最多的字元數」= 需替換數。若 ≤ k 可擴右；否則縮左。用 Counter 維護頻率，並維護「窗內最大頻率」以判斷是否合法。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)（字母固定數量）。

## 相關閱讀

- **演算法:** Sliding Window、Counter
