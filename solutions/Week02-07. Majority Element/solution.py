# LeetCode 169. Majority Element
# Time: O(n)  Space: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm.
        Maintain a candidate and a count. When count drops to 0,
        pick the current element as the new candidate. The majority
        element will always survive because it appears > n/2 times.
        """
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
