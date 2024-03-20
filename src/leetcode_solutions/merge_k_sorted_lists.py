"""
Solution for Merge k Sorted Lists problem
https://leetcode.com/problems/merge-k-sorted-lists/
"""

import heapq
from typing import List, Optional

from .util.list_node import ListNode


class Solution:
    """
    Solution for Merge k Sorted Lists problem
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists

        Args:
            lists (List[Optional[ListNode]]): List of linked lists

        Returns:
            Optional[ListNode]: Head of the merged linked list
        """
        head = tail = ListNode()
        heap = []

        for i, list_head in enumerate(lists):
            if list_head:
                heapq.heappush(heap, (list_head.val, i))
                lists[i] = list_head.next

        while heap:
            val, i = heapq.heappop(heap)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        return head.next
