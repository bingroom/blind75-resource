# Container With Most Water

**Topic:** Array

- **LeetCode:** [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i^th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

 

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

**Example 2:**

```

Input: height = [1,1]
Output: 1

```

 

**Constraints:**

	- `n == height.length`

	- `2 <= n <= 10^5`

	- `0 <= height[i] <= 10^4`

## Solution

```python
# LeetCode 11. Container With Most Water
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        兩條垂直線與 x 軸圍成容器，容量 = min(height[i], height[j]) * (j - i)。
        雙指針：從兩端往內，每次移動較短的那邊（因為容量由短邊決定）。
        """
        lo, hi = 0, len(height) - 1
        best = 0
        while lo < hi:
            w = hi - lo
            h = min(height[lo], height[hi])
            best = max(best, w * h)
            # 移動較短的一邊才有機會變大
            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
        return best

```

## 思路

- **雙指針：** 從兩端 `lo`, `hi` 開始，計算容量後，將**較短**的那邊往內移（因為容量由短邊決定，移短邊才有機會變大）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Two Pointers、Greedy
