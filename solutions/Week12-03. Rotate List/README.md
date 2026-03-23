# Rotate List

**Topic:** Linked List

- **LeetCode:** [61. Rotate List](https://leetcode.com/problems/rotate-list/)

## Problem Description
Given the `head` of a linked list, rotate the list to the right by `k` places.


## Solution

```python
# LeetCode 61. Rotate List
# Time: O(n)  Space: O(1)

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Effective rotation (k may exceed length)
        k %= length
        if k == 0:
            return head

        # Find the new tail: (length - k - 1) steps from head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Break the list
        tail.next = head      # Connect old tail to old head

        return new_head
```

## Approach
1. **Count the length** of the list and find the tail node in one pass.
2. **Reduce k:** Compute `k % length` since rotating by the full length is a no-op.
3. **Find the new tail:** Walk `length - k - 1` steps from the head. The node after this becomes the new head.
4. **Relink:** Break the list at the new tail, and connect the old tail to the old head.

This effectively moves the last `k` nodes to the front without any extra space.

## Complexity
- **Time:** O(n) -- two passes at most (one to count, one to find the split point).
- **Space:** O(1) -- only pointer variables.
