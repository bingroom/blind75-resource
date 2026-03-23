# Gas Station

**Topic:** Greedy

## Problem Description
There are n gas stations along a circular route. `gas[i]` is the amount of gas at station i and `cost[i]` is the gas needed to travel from station i to station i+1. Return the starting station index if you can complete the circuit, or -1.


## Solution

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

## Approach
First check feasibility: if total gas < total cost, return -1. Otherwise a solution is guaranteed to exist. Greedily track the tank balance. Whenever it drops below 0, the start must be after the current station. Reset the tank and start index.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
