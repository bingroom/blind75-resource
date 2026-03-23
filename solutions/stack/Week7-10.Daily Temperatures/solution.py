# LC 739. Daily Temperatures (Medium)
# https://leetcode.com/problems/daily-temperatures/
# Monotonic stack approach

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # monotonic decreasing stack of indices

        for i, temp in enumerate(temperatures):
            # Pop all indices whose temperature is less than current
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)

        return answer
