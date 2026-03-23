# Sort List

**Topic:** Linked List

- **LeetCode:** [148. Sort List](https://leetcode.com/problems/sort-list/)

## Problem Description
Given the `head` of a linked list, return the list after sorting it in ascending order. The problem asks for O(n log n) time and ideally O(1) space (though O(log n) for the recursion stack is acceptable).


## Solution

```python
# LeetCode 148. Sort List
# Time: O(n log n)  Space: O(log n) recursion stack

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty or single node
        if not head or not head.next:
            return head

        # Split the list into two halves
        mid = self._getMid(head)
        right_half = mid.next
        mid.next = None  # Cut the list

        left = self.sortList(head)
        right = self.sortList(right_half)
        return self._merge(left, right)

    def _getMid(self, head: ListNode) -> ListNode:
        """Return the node just before the midpoint (to split evenly)."""
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two sorted linked lists."""
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
```

## Approach
Use top-down merge sort, which naturally fits linked lists:

1. **Find the middle:** Use slow/fast pointers. Start `fast` one step ahead so `slow` lands on the last node of the left half.
2. **Split:** Cut the list at the midpoint by setting `mid.next = None`.
3. **Recurse:** Sort both halves independently.
4. **Merge:** Merge the two sorted halves using a standard two-pointer merge with a dummy head.

Merge sort is ideal for linked lists because the merge step requires no extra array allocation -- we just relink existing nodes.

## Complexity
- **Time:** O(n log n) -- standard merge sort recurrence.
- **Space:** O(log n) -- recursion stack depth. The merge itself is O(1) since we reuse existing nodes.
