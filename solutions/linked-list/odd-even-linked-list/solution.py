# LeetCode 328. Odd Even Linked List
# Time: O(n)  Space: O(1)

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even  # Save start of even list to append later

        while even and even.next:
            odd.next = even.next   # Link odd to next odd
            odd = odd.next
            even.next = odd.next   # Link even to next even
            even = even.next

        # Attach even list after odd list
        odd.next = even_head
        return head
