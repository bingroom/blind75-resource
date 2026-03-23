# LeetCode 658. Find K Closest Elements
# Time: O(log(n - k) + k)  Space: O(1) excluding output

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary search for the left boundary of the k-length window.
        The window starts at some index in [0, n - k]. For a candidate
        start `mid`, compare the distance of arr[mid] and arr[mid + k]
        to x: if arr[mid + k] is closer (or equal), shift right.
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # Compare which side is farther from x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
