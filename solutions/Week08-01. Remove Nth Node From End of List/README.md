# Remove Nth Node From End of List

**Topic:** Linked List

- **LeetCode:** [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

```

**Example 2:**

```

Input: head = [1], n = 1
Output: []

```

**Example 3:**

```

Input: head = [1,2], n = 1
Output: [1]

```

 

**Constraints:**

	- The number of nodes in the list is `sz`.

	- `1 <= sz <= 30`

	- `0 <= Node.val <= 100`

	- `1 <= n <= sz`

 

**Follow up:** Could you do this in one pass?

## Solution

```python
# LeetCode 19. Remove Nth Node From End of List
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        刪除倒數第 n 個節點。dummy + 快慢指針：快指針先走 n+1 步，再一起走，慢指針下一格即為待刪節點。
        """
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

```

## 思路

- **快慢指針：** 快指針先走 n+1 步（與慢指針間隔 n 個節點），再一起走直到快指針到 None，此時慢指針.next 即為倒數第 n 個，刪除即可。用 dummy 處理刪頭情況。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Two Pointers、Dummy Head
