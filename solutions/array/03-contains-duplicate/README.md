# Contains Duplicate

- **LeetCode:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

判斷陣列是否包含至少一個重複的數。

## 思路

- 用 **set** 存已見過的數，遍歷時若 `x in seen` 則回傳 `True`，否則 `seen.add(x)`。遍歷完回傳 `False`。
- 另解：排序後相鄰比較，時間 O(n log n)，空間 O(1)（若可改原陣列）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Set（集合）、Hash Table
