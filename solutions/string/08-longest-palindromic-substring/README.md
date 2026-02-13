# Longest Palindromic Substring

- **LeetCode:** [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求字串中最長迴文子字串（連續、正反讀相同）。

## 思路

- **中心擴展：** 以每個索引為「奇長迴文」中心、相鄰兩索引為「偶長迴文」中心，向外擴展直到不相等，記錄最長子字串。

## 時間 / 空間複雜度

- **時間:** O(n²)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Expand Around Center、Manacher（O(n) 進階）
