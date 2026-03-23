# Merge Two Sorted Lists

**Topic:** Linked List

- **LeetCode:** [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

```

**Example 2:**

```

Input: list1 = [], list2 = []
Output: []

```

**Example 3:**

```

Input: list1 = [], list2 = [0]
Output: [0]

```

 

**Constraints:**

	- The number of nodes in both lists is in the range `[0, 50]`.

	- `-100 <= Node.val <= 100`

	- Both `list1` and `list2` are sorted in **non-decreasing** order.

## Solution

```python
# LeetCode 21. Merge Two Sorted Lists
# 時間複雜度: O(m + n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

## 思路

- **Dummy 頭 + 雙指針：** 用 dummy 簡化邊界，每次比較兩鏈表頭，取較小者接到 cur，並移動該鏈表指針。最後接上剩餘部分。

## 時間 / 空間複雜度

- **時間:** O(m+n)。
- **空間:** O(1)（不計新節點）。

## 相關閱讀

- **資料結構:** Linked List、Merge
