# Swap Nodes in Pairs

**Topic:** Linked List
- **LeetCode 連結:** [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- **難度:** Medium

## 題目描述

給定一個鏈結串列，兩兩交換相鄰的節點並回傳。不能只改變節點的值，必須實際交換節點本身。

## 解題思路

1. 建立 dummy 節點指向 head，設 prev 指向 dummy。
2. 當 prev 後面至少有兩個節點時，取出 first 和 second。
3. 調整指標：first.next 指向 second 的下一個，second.next 指向 first，prev.next 指向 second。
4. 將 prev 移到已交換的第二個節點（即 first），繼續處理下一對。

## 程式碼

```python
# LeetCode 24. Swap Nodes in Pairs
# Time: O(n)  Space: O(1)

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second

            # Advance past the swapped pair
            prev = first

        return dummy.next
```

## 複雜度分析

- **時間複雜度:** O(n) -- each node is visited once.
- **空間複雜度:** O(1) -- only pointer manipulation, no extra data structures.
