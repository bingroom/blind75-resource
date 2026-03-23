# LeetCode 141. Linked List Cycle
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        判斷鏈表是否有環。Floyd 龜兔：快指針走 2、慢指針走 1，相遇則有環。
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
