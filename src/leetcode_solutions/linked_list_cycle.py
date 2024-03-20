"""
Solution for Linked List Cycle problem
https://leetcode.com/problems/linked-list-cycle/
"""

from typing import Optional

from .util.list_node import ListNode


class Solution:
    """
    Solution for Linked List Cycle problem
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Checks if the linked list has a cycle

        Args:
            head (ListNode): Head of the linked list

        Returns:
            bool: True if the linked list has a cycle, False otherwise
        """

        # Solution by modifying linked list
        # while head:
        #     if head.val == "seen":
        #         return True
        #     head.val = "seen"
        #     head = head.next

        # return False

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True

        return False
