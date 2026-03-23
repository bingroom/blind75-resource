# Remove Nth Node From End of List

**Topic:** Linked List
- **LeetCode 連結:** [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- **難度:** Medium

## 題目描述

給定一個鏈結串列，刪除從末尾算起的第 n 個節點，並回傳修改後的串列頭。要求一次遍歷完成。

## 解題思路

1. 建立一個 dummy 節點指向 head，用快慢雙指標從 dummy 出發。
2. 快指標先走 n+1 步，使快慢指標之間相距 n+1。
3. 快慢指標同時前進，直到快指標到達末尾。
4. 此時慢指標的下一個節點即為要刪除的節點，跳過它即可。

## 程式碼

```python
# LeetCode 19. Remove Nth Node From End of List
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
