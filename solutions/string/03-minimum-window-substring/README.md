# Minimum Window Substring

- **LeetCode:** [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求 s 中最短子字串，使得包含 t 中所有字元（次數至少與 t 相同）。

## 思路

- **滑動視窗：** 用 need = Counter(t) 表示還缺多少；右擴時減少 need，當「滿足條件的字元種類數」= len(need) 時嘗試縮左以得到最小窗，並更新起點與長度。

## 時間 / 空間複雜度

- **時間:** O(n + m)，n = len(s)，m = len(t)。
- **空間:** O(1)（字元集大小常數）。

## 相關閱讀

- **演算法:** Sliding Window、Hash Table、Counter
