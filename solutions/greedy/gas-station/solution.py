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
