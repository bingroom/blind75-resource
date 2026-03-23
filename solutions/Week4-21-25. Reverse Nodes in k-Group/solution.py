# LeetCode 25. Reverse Nodes in k-Group
# Time: O(n)  Space: O(1)

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Check if k nodes remain
            kth = self._getKth(group_prev, k)
            if not kth:
                break

            group_next = kth.next  # Node after this group

            # Reverse the group in-place
            prev, cur = kth.next, group_prev.next
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # Connect with previous part of list
            # group_prev.next was the first node, now the last after reversal
            tmp = group_prev.next
            group_prev.next = kth  # kth is now the first node of reversed group
            group_prev = tmp       # Move to end of reversed group

        return dummy.next

    def _getKth(self, cur: ListNode, k: int) -> Optional[ListNode]:
        """Return the k-th node after cur, or None if fewer than k remain."""
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
