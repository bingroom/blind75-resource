# Longest Substring Without Repeating Characters

- **LeetCode:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求字串中最長「不含重複字元」的連續子字串的長度。

## 思路

- **滑動視窗 + Set：** 右指針擴展，用 set 記錄視窗內字元；若新字元已存在則左指針往右縮直到該字元被移除，再擴右。過程中記錄最大視窗長度。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(min(n, |Σ|))，Σ 為字元集。

## 相關閱讀

- **演算法:** Sliding Window、Hash Set
- **資料結構:** Set
