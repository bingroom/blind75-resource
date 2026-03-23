# Reorder List

- **LeetCode:** [143. Reorder List](https://leetcode.com/problems/reorder-list/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You are given the head of a singly linked-list. The list can be represented as:

```

L0 → L1 → … → Ln - 1 → Ln

```

*Reorder the list to be on the following form:*

```

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

```

Input: head = [1,2,3,4]
Output: [1,4,2,3]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

```

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

```

 

**Constraints:**

	- The number of nodes in the list is in the range `[1, 5 * 10^4]`.

	- `1 <= Node.val <= 1000`

## Solution

```python
# LeetCode 143. Reorder List
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

## 思路

- **找中點**（快慢指針）→ **反轉後半段** → **兩段交錯合併**（前半與反轉後的後半一節一節接）。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** 找中點、反轉鏈表、合併
