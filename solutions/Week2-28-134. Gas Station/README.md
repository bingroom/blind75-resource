# Gas Station

**Topic:** Array
- **LeetCode 連結:** [134. Gas Station](https://leetcode.com/problems/gas-station/)
- **難度:** Medium

## 題目描述

在一條環形路線上有 n 個加油站，每站可加 gas[i] 的油，從第 i 站到第 i+1 站需耗油 cost[i]。求從哪個站出發可以繞行一圈，若無法完成則回傳 -1。

## 解題思路

1. 若總加油量小於總耗油量，則不可能完成，回傳 -1。
2. 使用貪心法從頭遍歷，維護當前油箱餘量。
3. 若油箱餘量變為負數，代表從 start 到當前站之間的任何站都不可行，將起點設為下一站。
4. 遍歷結束後，start 即為唯一可行的起點。

## 程式碼

```python
# LeetCode 134. Gas Station
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas < total cost, no solution exists
        if sum(gas) < sum(cost):
            return -1

        # Greedy: start from the station after the one where tank goes negative
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # Can't start from any station in [start, i], try i+1
                start = i + 1
                tank = 0

        return start
```

## 複雜度分析

- **時間複雜度:** O(n)
- **空間複雜度:** O(1)
