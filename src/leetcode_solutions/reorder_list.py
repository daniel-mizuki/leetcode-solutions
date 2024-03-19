"""Solution for Reorder List problem"""

from typing import Optional

from .util.list_node import ListNode


class Solution:
    """Solution for Reorder List problem"""

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Use stack to reverse linked list
        # stack = []
        # node = head
        # while node:
        #     stack.append(node)
        #     node = node.next

        # while head and head.next:
        #     insert_node = stack.pop()
        #     stack[-1].next = None
        #     next_node = head.next
        #     insert_node.next = next_node
        #     head.next = insert_node
        #     head = next_node

        # Reverse second half of linked list in place
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = self.reverse_list(slow.next)
        slow.next = None

        while second:
            first_next, second_next = first.next, second.next
            first.next, second.next = second, first_next
            first, second = first_next, second_next

    def reverse_list(self, head):
        """
        Reverse linked list

        Args:
            head (ListNode): Head of the linked list
        """
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev
