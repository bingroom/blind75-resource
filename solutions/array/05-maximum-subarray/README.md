# Maximum Subarray

- **LeetCode:** [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- **NeetCode 練習:** [Blind 75](https://neetcode.io/problems?list=blind75)

## 題意

求陣列中「連續子陣列」的最大和（至少取一個元素）。

## 思路

- **Kadane 演算法：** 定義 `cur` = 以「目前位置」為結尾的最大子陣列和。每次要麼接上前面 (`cur + nums[i]`)，要麼從這裡重啟 (`nums[i]`)，取較大者；再以 `best` 記錄全域最大。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Kadane's Algorithm、動態規劃 (DP) 一維
