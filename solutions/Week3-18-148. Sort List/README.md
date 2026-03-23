# Sort List

**Topic:** Linked List
- **LeetCode 連結:** [148. Sort List](https://leetcode.com/problems/sort-list/)
- **難度:** Medium

## 題目描述

給定一個鏈結串列的頭節點，將其按升序排列並回傳排序後的鏈結串列。要求時間複雜度 O(n log n)。

## 解題思路

1. 使用快慢指標找到鏈結串列的中點。
2. 從中點斷開，將串列分成兩半。
3. 遞迴排序左半和右半。
4. 使用合併排序將兩個已排序的串列合併。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n log n) -- standard merge sort recurrence.
- **空間複雜度:** O(log n) -- recursion stack depth. The merge itself is O(1) since we reuse existing nodes.
