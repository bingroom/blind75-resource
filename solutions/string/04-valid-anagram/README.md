# Valid Anagram

- **LeetCode:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

判斷 t 是否為 s 的 anagram（由相同字元、相同次數組成，順序可不同）。

## 思路

- **計數：** 比較兩字串的字元頻率是否相同，例如 `Counter(s) == Counter(t)`。長度不同可先直接回傳 False。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)（字母表固定）。

## 相關閱讀

- **資料結構:** Hash Table、Counter
