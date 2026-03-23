# Add Two Numbers

- **LeetCode:** [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.


## Solution

```python
# LeetCode 2. Add Two Numbers
# Time: O(max(m, n))  Space: O(max(m, n))

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carry, digit = divmod(val, 10)
            cur.next = ListNode(digit)
            cur = cur.next

        return dummy.next
```

## Approach
1. Traverse both lists simultaneously, summing corresponding digits along with a carry.
2. Use `divmod(sum, 10)` to get the new carry and the current digit.
3. Create a new node for each digit and append it to the result list.
4. Continue until both lists are exhausted and carry is zero.

The reverse storage order is convenient -- it means we naturally process digits from least significant to most significant, just like manual addition.

## Complexity
- **Time:** O(max(m, n)) where m and n are the lengths of the two lists.
- **Space:** O(max(m, n)) for the output list.
