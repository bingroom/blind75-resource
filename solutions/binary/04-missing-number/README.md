# Missing Number

- **LeetCode:** [268. Missing Number](https://leetcode.com/problems/missing-number/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

陣列長度 n，元素為 [0, n] 中不重複的 n 個數，找缺的那一個數。

## 思路

- **數學：** 預期和 = 0+1+...+n = n(n+1)/2，減去陣列實際和即為缺的數。
- **位元：** 用 XOR，把 0..n 與所有 nums 做 XOR，最後剩下缺的數。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Math、XOR 性質（可選）
