# Add Two Numbers

**Topic:** Linked List
- **LeetCode 連結:** [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- **難度:** Medium

## 題目描述

給定兩個以反向鏈結串列表示的非負整數，將它們相加並以相同格式回傳結果鏈結串列。

## 解題思路

1. 同時遍歷兩個鏈結串列，逐位相加並追蹤進位。
2. 每一位的值為兩節點值加上進位，取餘數為當前位，商為新進位。
3. 建立新節點串接結果，直到兩串列皆為空且無進位。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(max(m, n)) where m and n are the lengths of the two lists.
- **空間複雜度:** O(max(m, n)) for the output list.
