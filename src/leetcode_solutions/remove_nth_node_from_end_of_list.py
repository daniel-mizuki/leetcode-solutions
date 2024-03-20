"""
Solution for Remove Nth Node From End of List problem
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional

from .util.list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list

        Args:
            head (ListNode): Head of the linked list
            n (int): The index from the end of the list of the node to remove

        Returns:
            ListNode: The head of the new linked list
        """

        # prev = node = ListNode()
        # prev.next = head
        # tail = head

        # while tail:
        #     if n > 0:
        #         n -= 1
        #     elif n == 0:
        #         node = node.next

        #     tail = tail.next

        # if node.next and n == 0:
        #     node.next = node.next.next

        # return prev.next

        # Alternative solution
        prev = node = ListNode(-1, head)
        tail = head

        for _ in range(n):
            if not tail:
                return head
            tail = tail.next

        while tail:
            tail = tail.next
            node = node.next

        node.next = node.next.next if node.next else None

        return prev.next
