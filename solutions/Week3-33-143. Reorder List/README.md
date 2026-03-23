# Reorder List

**Topic:** Linked List
- **LeetCode 連結:** [143. Reorder List](https://leetcode.com/problems/reorder-list/)
- **難度:** Medium

## 題目描述

給定一個單向鏈結串列 L0→L1→...→Ln，將其重排為 L0→Ln→L1→Ln-1→...。需原地操作。

## 解題思路

1. 使用快慢指標找到鏈結串列中點。
2. 從中點斷開，將後半段原地反轉。
3. 將前半段和反轉後的後半段交錯合併。

## 程式碼

```python
# LeetCode 143. Reorder List
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        將鏈表改為 L0 -> Ln -> L1 -> Ln-1 -> ...。找中點、反轉後半、交錯合併。
        """
        if not head or not head.next:
            return
        # 找中點（慢指針到中點）
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 反轉後半
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # 交錯合併
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
