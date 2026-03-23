# Middle of the Linked List

- **LeetCode:** [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

## Problem Description
Given the `head` of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.


## Solution

```python
# LeetCode 876. Middle of the Linked List
# Time: O(n)  Space: O(1)

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Slow/fast pointer: when fast reaches end, slow is at middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## Approach
Use the slow/fast pointer technique:
1. Initialize both `slow` and `fast` to `head`.
2. Move `slow` one step and `fast` two steps each iteration.
3. When `fast` reaches the end (or goes past it), `slow` is at the middle.

For even-length lists, `slow` naturally lands on the second of the two middle nodes, which is what the problem requires.

## Complexity
- **Time:** O(n) -- single pass through the list.
- **Space:** O(1) -- only two pointers.
