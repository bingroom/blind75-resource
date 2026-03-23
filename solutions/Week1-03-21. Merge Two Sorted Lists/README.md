# Merge Two Sorted Lists

**Topic:** Linked List
- **LeetCode 連結:** [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- **難度:** Easy

## 題目描述

給定兩條已排序的鏈結串列，將它們合併為一條新的已排序鏈結串列。新串列應由兩條串列的節點拼接而成。

## 解題思路

1. 建立一個虛擬頭節點（dummy node）作為新串列的起點。
2. 同時遍歷兩條串列，每次比較兩邊的當前節點，將較小者接到新串列尾端。
3. 當其中一條串列遍歷完畢，將另一條的剩餘部分直接接上。
4. 回傳虛擬頭節點的 next，即為合併後的串列。

## 程式碼

```python
# LeetCode 21. Merge Two Sorted Lists
# 時間複雜度: O(m + n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        合併兩條已排序鏈表。dummy 頭，每次取兩邊較小者接上。
        """
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next
```

## 複雜度分析

- **時間複雜度:** O(m+n)。
- **空間複雜度:** O(1)（不計新節點）。
