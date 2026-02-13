# Binary Tree Maximum Path Sum

- **LeetCode:** [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求二元樹中「任意節點到任意節點」路徑的最大和（路徑可經由根、不必從根到葉）。

## 思路

- **遞迴：** 定義「以該節點為端點」往下的最大單邊路徑和。對每個節點，用「左單邊 + 根 + 右單邊」更新全域最大；回傳值為根 + max(左, 右)（若子樹為負則取 0）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(h)。

## 相關閱讀

- **演算法:** Tree DP、後序遍歷
