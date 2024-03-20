"""
Singly Linked List Node
"""


class ListNode:
    """Linked List Node"""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None
        head = curr = cls(lst[0])
        for val in lst[1:]:
            curr.next = cls(val)
            curr = curr.next
        return head

    def __eq__(self, other) -> bool:
        node = self
        while node and other:
            if node.val != other.val:
                return False
            node = node.next
            other = other.next
        return not (other or node)

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"
