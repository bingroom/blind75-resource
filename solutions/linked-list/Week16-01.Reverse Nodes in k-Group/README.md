# Reverse Nodes in k-Group

- **LeetCode:** [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Problem Description
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list. If the number of nodes is not a multiple of `k`, the remaining nodes at the end stay in their original order. Only node links may be changed, not node values.


## Solution

```python
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
```

## Approach
1. Use a dummy node before the head and track `group_prev` (the node before each k-group).
2. For each group, first check if `k` nodes remain by walking forward `k` steps. If not, stop.
3. Reverse the `k` nodes in-place using the standard iterative reversal. Set `prev` to the node after the group so the reversed segment links forward correctly.
4. Update `group_prev.next` to point to `kth` (the new first node of the reversed group).
5. Advance `group_prev` to the old first node (now the last node of the reversed group).

## Complexity
- **Time:** O(n) -- each node is visited a constant number of times (once to check length, once to reverse).
- **Space:** O(1) -- all operations are pointer manipulation in-place.
