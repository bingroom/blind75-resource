# Reverse Nodes in k-Group

**Topic:** Linked List
- **LeetCode 連結:** [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- **難度:** Hard

## 題目描述

給定一個鏈結串列，每 k 個節點為一組進行反轉。若剩餘節點不足 k 個則保持原序。

## 解題思路

1. 先檢查剩餘節點是否足夠 k 個。
2. 若足夠，將該組 k 個節點原地反轉。
3. 將反轉後的組與前後部分正確連結。
4. 移動到下一組，重複操作直到剩餘不足 k 個。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) -- each node is visited a constant number of times (once to check length, once to reverse).
- **空間複雜度:** O(1) -- all operations are pointer manipulation in-place.
