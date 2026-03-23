# Rotate List

**Topic:** Linked List
- **LeetCode 連結:** [61. Rotate List](https://leetcode.com/problems/rotate-list/)
- **難度:** Medium

## 題目描述

給定一個鏈結串列和整數 k，將串列向右旋轉 k 個位置。

## 解題思路

1. 先遍歷串列計算長度並找到尾節點。
2. 取 k 對長度的餘數，處理 k 大於長度的情況。
3. 找到新的尾節點（從頭走 length - k - 1 步），其下一個節點為新的頭。
4. 斷開連結並將舊尾接到舊頭，形成旋轉結果。

## 程式碼

```python
# LeetCode 61. Rotate List
# Time: O(n)  Space: O(1)

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Effective rotation (k may exceed length)
        k %= length
        if k == 0:
            return head

        # Find the new tail: (length - k - 1) steps from head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Break the list
        tail.next = head      # Connect old tail to old head

        return new_head
```

## 複雜度分析

- **時間複雜度:** O(n) -- two passes at most (one to count, one to find the split point).
- **空間複雜度:** O(1) -- only pointer variables.
