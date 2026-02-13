# Jump Game

- **LeetCode:** [55. Jump Game](https://leetcode.com/problems/jump-game/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

從索引 0 出發，nums[i] 表示在 i 可跳的最遠步數，判斷能否到達最後一格。

## 思路

- **貪心：** 維護「目前能到達的最遠索引」reach。若 i > reach 則無法到達；否則用 i + nums[i] 更新 reach。到最後即 True。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Greedy、Reachability
