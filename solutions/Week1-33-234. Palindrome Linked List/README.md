# Palindrome Linked List

**Topic:** Linked List
- **LeetCode 連結:** [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
- **難度:** Easy

## 題目描述

給定一個單向鏈結串列，判斷它是否為迴文。要求 O(1) 額外空間。

## 解題思路

1. 使用快慢指標找到鏈結串列中點。
2. 將後半段鏈結串列原地反轉。
3. 從頭和從反轉後的後半段同時遍歷比較，若所有值相等則為迴文。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) -- one pass to find middle, one pass to reverse, one pass to compare.
- **空間複雜度:** O(1) -- only pointer variables, no extra data structures.
