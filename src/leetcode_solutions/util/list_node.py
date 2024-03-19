"""
Singly Linked List Node
"""


class ListNode:
    """Linked List Node"""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __eq__(self, other) -> bool:
        node = self
        while node and other:
            if node.val != other.val:
                return False
            node = node.next
            other = other.next
        return not (other or node)
