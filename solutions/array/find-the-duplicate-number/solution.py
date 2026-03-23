# LeetCode 287. Find the Duplicate Number
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Tortoise and Hare (cycle detection).
        Treat each value as a pointer to another index.
        Since there are n+1 values in range [1, n], a cycle must exist,
        and the entrance to the cycle is the duplicate number.
        """
        # Phase 1: detect the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the cycle entrance
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
