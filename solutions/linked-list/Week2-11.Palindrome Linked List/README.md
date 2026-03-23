# Palindrome Linked List

- **LeetCode:** [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

## Problem Description
Given the `head` of a singly linked list, return `true` if it is a palindrome, or `false` otherwise.


## Solution

```python
# LeetCode 234. Palindrome Linked List
# Time: O(n)  Space: O(1)

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle using slow/fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half in-place
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare first half with reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
```

## Approach
1. Use slow/fast pointers to find the middle of the list.
2. Reverse the second half of the list in-place.
3. Compare the first half with the reversed second half node by node.
4. If all values match, the list is a palindrome.

This avoids using O(n) extra space by modifying the list in-place rather than copying values to an array.

## Complexity
- **Time:** O(n) -- one pass to find middle, one pass to reverse, one pass to compare.
- **Space:** O(1) -- only pointer variables, no extra data structures.
