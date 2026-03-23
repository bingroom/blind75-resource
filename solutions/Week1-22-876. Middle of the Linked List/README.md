# Middle of the Linked List

**Topic:** Linked List
- **LeetCode 連結:** [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- **難度:** Easy

## 題目描述

給定一個單向鏈結串列的頭節點，回傳中間節點。若有兩個中間節點，回傳第二個中間節點。

## 解題思路

1. 使用快慢指標，slow 和 fast 都從 head 出發。
2. 每次 slow 前進一步，fast 前進兩步。
3. 當 fast 到達尾端（fast 為 None 或 fast.next 為 None）時，slow 恰好在中間位置。
4. 回傳 slow 即為中間節點。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n) -- single pass through the list.
- **空間複雜度:** O(1) -- only two pointers.
