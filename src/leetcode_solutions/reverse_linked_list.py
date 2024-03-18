"""Solution for Reverse Linked List problem"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """Linked List Node"""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __eq__(self, other) -> bool:
        node = self
        while node:
            if node.val != other.val:
                return False
            node = node.next
            other = other.next
        return not other


class Solution:
    """Solution for Reverse Linked List problem"""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and
        return the reversed list.

        Args:
            head (ListNode): Head of the linked list

        Returns:
            ListNode: Reversed linked list
        """
        # Iterative implementation
        prev_head = None

        while head:
            next_node = head.next
            head.next = prev_head
            prev_head = head
            head = next_node

        return prev_head

        # Recursive implementation
        # if not head:
        #     return None

        # rest = head.next
        # head.next = None

        # return self.reverse_list_helper(head, rest)

    # Helper method for recursive implementation
    # def reverse_list_helper(self, reversed_head, rest):
    #     if not rest:
    #         return reversed_head

    #     rest_next = rest.next
    #     rest.next = reversed_head

    #     return self.reverse_list_helper(rest, rest_next)
