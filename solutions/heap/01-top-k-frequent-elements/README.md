# Top K Frequent Elements

- **LeetCode:** [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

回傳陣列中出現頻率前 k 高的元素（順序不拘）。

## 思路

- **Counter + Min-Heap：** 先計數，再維護大小為 k 的 min-heap（以頻率為鍵），遍歷時若超過 k 個就 pop 最小；最後 heap 中即為前 k 大頻率對應的數。或使用桶排序（頻率當桶）可 O(n)。

## 時間 / 空間複雜度

- **時間:** O(n log k)。
- **空間:** O(n)。

## 相關閱讀

- **資料結構:** Heap、Counter
- **演算法:** Top K、Quick Select 可選
