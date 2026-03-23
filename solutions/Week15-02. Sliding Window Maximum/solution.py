# LC 239. Sliding Window Maximum (Hard)
# https://leetcode.com/problems/sliding-window-maximum/
# Monotonic deque approach

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # monotonic decreasing deque of indices
        result = []

        for i, num in enumerate(nums):
            # Remove indices that have fallen out of the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order: remove smaller elements from back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)

            # Start recording results once we have a full window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
