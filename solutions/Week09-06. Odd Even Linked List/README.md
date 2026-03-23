# Odd Even Linked List

**Topic:** Linked List

- **LeetCode:** [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

## Problem Description
Given the `head` of a singly linked list, group all nodes with odd indices together followed by nodes with even indices, and return the reordered list. The first node is considered odd, the second node even, and so on. Solve in O(1) extra space and O(n) time.


## Solution

```python
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
```

## Approach
1. Maintain two pointers: `odd` starting at the first node, `even` starting at the second.
2. Save the head of the even list (`even_head`).
3. In each iteration, link the current odd node to the next odd node (skipping even), then link the current even node to the next even node (skipping odd).
4. After the loop, attach the even list to the end of the odd list.

## Complexity
- **Time:** O(n) -- single pass through the list.
- **Space:** O(1) -- rearranges nodes in-place with only pointer variables.
