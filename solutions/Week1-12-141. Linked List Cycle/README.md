# Linked List Cycle

**Topic:** Linked List
- **LeetCode 連結:** [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- **難度:** Easy

## 題目描述

給定一個鏈結串列的頭節點 `head`，判斷該串列中是否存在環。若某個節點可以透過不斷追蹤 `next` 再次到達，則表示存在環。

## 解題思路

1. 使用 Floyd 龜兔演算法，設定快慢兩個指針都從 `head` 出發。
2. 慢指針每次走一步，快指針每次走兩步。
3. 若快指針到達尾端（`None`），表示無環，回傳 `False`。
4. 若快慢指針相遇，表示有環，回傳 `True`。

## 程式碼

```python
# LeetCode 141. Linked List Cycle
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        判斷鏈表是否有環。Floyd 龜兔：快指針走 2、慢指針走 1，相遇則有環。
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(1)。
