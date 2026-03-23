# Odd Even Linked List

**Topic:** Linked List
- **LeetCode 連結:** [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)
- **難度:** Medium

## 題目描述

給定一個單向鏈結串列，將所有奇數位置的節點排在前面，偶數位置的節點排在後面。要求使用 O(1) 額外空間和 O(n) 時間。

## 解題思路

1. 設 odd 指向第一個節點，even 指向第二個節點，並記錄偶數鏈的頭。
2. 交替地將 odd.next 指向 even 的下一個（下一個奇數），even.next 指向再下一個（下一個偶數）。
3. 推進 odd 和 even 指標，直到偶數鏈結束。
4. 將奇數鏈的尾端接上偶數鏈的頭，完成重組。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) -- single pass through the list.
- **空間複雜度:** O(1) -- rearranges nodes in-place with only pointer variables.
