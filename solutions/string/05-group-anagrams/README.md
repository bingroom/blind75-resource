# Group Anagrams

- **LeetCode:** [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

將字串陣列中所有互為 anagram 的字串分到同一組，回傳各組。

## 思路

- **分組 key：** 將每個字串排序後當 key（或使用 tuple 字元計數），相同 key 的放同一組。用 defaultdict(list) 收集。

## 時間 / 空間複雜度

- **時間:** O(n · k log k)，n 為字串數，k 為最長字串長度（排序）。
- **空間:** O(n · k) 存輸出。

## 相關閱讀

- **資料結構:** Hash Table、defaultdict
- **演算法:** 排序當 key
