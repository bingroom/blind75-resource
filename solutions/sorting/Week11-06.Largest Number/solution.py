# LeetCode 179. Largest Number
# Time: O(n log n)  Space: O(n)

import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator: compare a+b vs b+a as strings
        strs = [str(num) for num in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        strs.sort(key=functools.cmp_to_key(compare))

        # Edge case: all zeros
        if strs[0] == '0':
            return '0'

        return ''.join(strs)
