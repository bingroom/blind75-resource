# LeetCode 278. First Bad Version
# Time: O(log n)  Space: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                hi = mid          # mid might be the first bad version
            else:
                lo = mid + 1      # mid is good, search right half
        return lo
