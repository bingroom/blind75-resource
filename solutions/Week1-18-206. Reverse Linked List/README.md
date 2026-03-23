# Reverse Linked List

**Topic:** Linked List
- **LeetCode 連結:** [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- **難度:** Easy

## 題目描述

給定一個單向鏈結串列的頭節點，將整個鏈結串列反轉後回傳新的頭節點。

## 解題思路

1. 初始化 prev 為 None，用來記錄前一個節點。
2. 遍歷鏈結串列，先暫存 head.next，再將 head.next 指向 prev。
3. 將 prev 移到 head，head 移到下一個節點，重複直到結束。
4. 回傳 prev 作為新的頭節點。

## 程式碼

```python
# LeetCode 206. Reverse Linked List
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反轉單向鏈表。迭代：維護 prev，每次把 cur.next 指到 prev，再前進。
        """
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
