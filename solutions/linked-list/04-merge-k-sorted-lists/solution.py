# LeetCode 23. Merge K Sorted Lists
# 時間複雜度: O(N log k)  N=總節點數, k=鏈表數  空間複雜度: O(k)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        合併 k 條已排序鏈表。用 min-heap 存每條的頭，每次 pop 最小、接上並把該鏈下一節點 push。
        """
        dummy = ListNode(0)
        cur = dummy
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
