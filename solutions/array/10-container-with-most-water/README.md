# Container With Most Water

- **LeetCode:** [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

給定高度陣列，選兩條線與 x 軸圍成容器，求最大容量（寬 × 較矮的高度）。

## 思路

- **雙指針：** 從兩端 `lo`, `hi` 開始，計算容量後，將**較短**的那邊往內移（因為容量由短邊決定，移短邊才有機會變大）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Two Pointers、Greedy
