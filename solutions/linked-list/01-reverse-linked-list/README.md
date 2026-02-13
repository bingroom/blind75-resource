# Reverse Linked List

- **LeetCode:** [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```

Input: head = [1,2]
Output: [2,1]

```

**Example 3:**

```

Input: head = []
Output: []

```

 

**Constraints:**

	- The number of nodes in the list is the range `[0, 5000]`.

	- `-5000 <= Node.val <= 5000`

 

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solution

```python
# LeetCode 206. Reverse Linked List
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

## 思路

- **迭代：** prev = None，每次把當前節點的 next 改為 prev，再 prev=cur、cur=原 next，直到 cur 為 None，回傳 prev。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **資料結構:** Linked List、指針操作
