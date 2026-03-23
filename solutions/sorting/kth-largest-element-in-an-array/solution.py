# LeetCode 215. Kth Largest Element in an Array
# Time: O(n log k)  Space: O(k)

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
