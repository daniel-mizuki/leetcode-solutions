"""Solution for Merge Two Sorted Lists problem"""

from typing import Optional

from .util.list_node import ListNode


class Solution:
    """Solution for Merge Two Sorted Lists problem"""

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists

        Args:
            list1 (ListNode): Head of the first linked list
            list2 (ListNode): Head of the second linked list

        Returns:
            ListNode: Head of the merged linked list
        """
        # Recursive implementation
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        # if list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2

        dummy_node = ListNode(0)
        tail = dummy_node

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy_node.next
